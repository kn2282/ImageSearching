from .ModelDetector import ModelDetector
from PIL import Image
import json
from .SearchAlgorithm import *


class ImageSearcher:
    def __init__(self, model: ModelDetector, algorithm: SearchAlgorithm, confidence_level: float, model_name: ''):
        self._model = model
        self._algorithm = algorithm
        self._confidence_level = confidence_level
        self.model_name = model_name

    def searchImage(self, path):
        """
        Method to search one image
        :param path: photo path
        :return: array of cropped photos from original photos that contain searched objects and max confidence of those
        """
        im: Image.Image = Image.open(path)
        im_size = im.size
        found = []
        confidence = 0.0
        for xs, ys in self._algorithm.get_algorithm(im_size):
            im_resized = im.crop(
                (int(im_size[0] * xs[0]), int(im_size[1] * ys[0]), int(im_size[1] * ys[1]), int(im_size[0] * xs[1])))
            conf = self._model.predict(im_resized)
            if conf > self._confidence_level:
                if confidence < conf:
                    confidence = conf
                found.append((xs, ys))

        return found, confidence

    def save(self):
        """
        Method to save parameters of a model
        """
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
        """
        :param name: HALF_IMAGES or QUARTER_IMAGES
        :return: Dict with values attributed to name
        """
        if name == AlgorithmType.HALF_IMAGES['name']:
            return AlgorithmType.HALF_IMAGES

        if name == AlgorithmType.QUARTER_IMAGES['name']:
            return AlgorithmType.QUARTER_IMAGES

    @staticmethod
    def load(path: '', max_depth=None, alg_type=None, confidence_level=None):
        """
        Method used to load trained model for SetSearcher
        :param path: parameters path
        :param max_depth: variable passed to ImageSearcher, the bigger the more precisely an image is searched
        :param alg_type: HALF_IMAGES or QUARTER_IMAGES
        :param confidence_level: acceptance rate of an image
        :return:
        """
        with open(path, "r") as read_file:
            parameters_dict = json.load(read_file)

            model_detect: ModelDetector = ModelDetector(
                load_model=(parameters_dict["model_path"], parameters_dict["img_size"])
            )

            if max_depth is None:
                max_depth = parameters_dict["max_depth"]

            if alg_type is None:
                alg_type = ImageSearcher.__name_to_type(parameters_dict["algorithm_type"])
            elif isinstance(alg_type, type("")):
                alg_type = ImageSearcher.__name_to_type(alg_type)

            search_alg = SearchAlgorithm(
                alg_type=alg_type,
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
