from ModelDetector import ModelDetector
from PIL import Image
import json

class AlgorithmType:
    HALF_IMAGES = {
        'name': 'HALF_IMAGES',
        'n_pictures_in_depth': lambda max_depth: [2 ** i for i in range(max_depth + 1)],
        'prop_divider_func': lambda x: 2 / (x + 1),
        'pic_shift': 1/2
    }
    QUARTER_IMAGES = {
        'name': 'QUARTER_IMAGES',
        'n_pictures_in_depth': lambda max_depth: [1.5 ** i for i in range(max_depth + 1)],
        'prop_divider_func': lambda x: 4 / (x + 3),
        'pic_shift': 1/4
    }





class SearchAlgorithm:
    def __init__(self, type: AlgorithmType, model_input_prop: float = 1, max_depth: int = 4):
        """

        :type max_depth: max depth of searchimg inside picture.
         Bigger depth -> algorithm searches to smaller pice of picture
        """

        self.max_depth = max_depth
        self.model_input_prop = model_input_prop
        self.type = type

        self.__n_pictures_in_depth = type['n_pictures_in_depth'](max_depth)
        self.__prop_divider_func = type['prop_divider_func']
        self.__pic_shift = type['pic_shift']

    @staticmethod
    def __generator(x_frame_prop, y_frame_prop, n_pictures_in_depth, divider_func, pic_shift, max_depth):

        for depth in range( max_depth + 1):
            n_pic = n_pictures_in_depth[depth]

            x_prop = x_frame_prop * divider_func(n_pic)

            y_prop = y_frame_prop * divider_func(n_pic)

            x, y = 0, 0
            while y + y_prop < 1:
                while x + x_prop < 1:
                    yield (x, x + x_prop), (y, y + y_prop)
                    x += x_prop * pic_shift

                yield (1 - x_prop, 1), (y, y + y_prop)
                y += y_prop * pic_shift

            while x + x_prop < 1:
                yield (x, x + x_prop), (1 - y_prop, 1)
                x += x_prop * pic_shift

            yield (1 - x_prop, 1), (1 - y_prop, 1)

    def get_algorithm(self, img_prop: float):
        """

        :type img_prop: proportions x to y (width to height)
        """
        if isinstance(img_prop, (type(()), type([]))):
            img_prop = img_prop[0] / img_prop[1]

        if img_prop > self.model_input_prop:
            main_y_prop = 1.
            main_x_prop = self.model_input_prop / img_prop
        else:
            main_x_prop = 1.
            main_y_prop = img_prop / self.model_input_prop

        return self.__generator(
            main_x_prop,
            main_y_prop,
            self.__n_pictures_in_depth,
            self.__prop_divider_func,
            self.__pic_shift,
            self.max_depth
        )



class ImageSearcher:
    def __init__(self, model: ModelDetector, algorithm: SearchAlgorithm, confidence_level: float, model_name:''):
        self._model = model
        self._algorithm = algorithm
        self._confidence_level = confidence_level
        self.model_name = model_name

    def searchImage(self, path, return_confidence=True):
        im: Image.Image = Image.open(path)
        im_size = im.size
        found = []
        confidence = 0.0
        for xs, ys in self._algorithm.get_algorithm(im_size):
            im_resized = im.crop((int(im_size[0]*xs[0]), int(im_size[1]*ys[0]), int(im_size[1]*ys[1]), int(im_size[0]*xs[1])))
            conf = self._model.predict(im_resized)
            if conf > self._confidence_level:
                if confidence < conf and return_confidence:
                    confidence = conf
                found.append((xs, ys))

        if return_confidence:
            return found, confidence
        else:
            return found


    def save(self):
        parameters_dict = dict()
        parameters_dict["model_name"] = self.model_name
        parameters_dict["algorithm_type"] = self._algorithm.type['name']
        parameters_dict["max_depth"] = self._algorithm.max_depth
        parameters_dict["confidence_level"] = self._confidence_level
        save_path = f"keras_models/{self.model_name}_model"
        parameters_dict["model_path"] = save_path
        parameters_dict["img_size"] = self._model._img_size
        self._model.save(save_path)
        with open(f"models/{self.model_name}_parameters.json", "w") as write_file:
            json.dump(parameters_dict, write_file)

    @staticmethod
    def __name_to_type(name: ''):
        if name == AlgorithmType.HALF_IMAGES['name']:
            return AlgorithmType.HALF_IMAGES

        if name == AlgorithmType.QUARTER_IMAGES['name']:
            return AlgorithmType.QUARTER_IMAGES

    @staticmethod
    def load(path: '', search_alg=None, max_depth=None, alg_type=None, confidence_level=None):
        with open(path, "r") as read_file:
            parameters_dict = json.load(read_file)

            model_detect: ModelDetector = ModelDetector(
                load_model=(parameters_dict["model_path"], parameters_dict["img_size"])
            )

            if max_depth is None:
                max_depth = parameters_dict["max_depth"]

            if alg_type is None:
                alg_type = ImageSearcher.__name_to_type(parameters_dict["algorithm_type"])

            if search_alg is None:
                search_alg = SearchAlgorithm(
                    type=alg_type,
                    model_input_prop=parameters_dict["img_size"][0] / parameters_dict["img_size"][1],
                    max_depth=max_depth
                )

            if confidence_level is None:
                confidence_level = parameters_dict["confidence_level"]

            return ImageSearcher(
                model=model_detect,
                algorithm=search_alg,
                confidence_level=confidence_level,
                model_name=parameters_dict["model_name"]
            )



