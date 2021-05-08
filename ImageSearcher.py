from math import isclose

class AlgorithmType:
    HALF_IMAGES = 1
    QUARTER_IMAGES = 2
    HORIZONTAL = 3
    VERTICAL = 4


class SearchAlgorithm:
    def __init__(self, type: AlgorithmType, model_input_prop: float = 1, max_depth: int = 4):
        """

        :type max_depth: max depth of saerchimg inside picture.
         Bigger depth -> algorithm searches to smaller pice of picture
        """
        self.max_depth = max_depth
        self.model_input_prop = model_input_prop
        self.type = type

        if type == AlgorithmType.HALF_IMAGES:
            self.__n_pictures_in_depth = [2 ** i for i in range(max_depth + 1)]
            self.__prop_divider_func = lambda x: 2 / (x + 1)
            self.__pic_shift = 1/2

        if type == AlgorithmType.QUARTER_IMAGES:
            self.__n_pictures_in_depth = [2 ** i for i in range(max_depth + 1)]
            self.__prop_divider_func = lambda x: 4 / (x + 3)
            self.__pic_shift = 1/4

    @staticmethod
    def __scrap_shift(frame_prop, scrap_prop, n_scraps):
        return (frame_prop - scrap_prop) / (n_scraps - 1)

    @staticmethod
    def __generator(x_frame_prop, y_frame_prop, n_pictures_in_depth, divider_func, pic_shift, max_depth):

        for depth in range( max_depth + 1):
            n_pic = n_pictures_in_depth[depth]

            x_prop = x_frame_prop * divider_func(n_pic)
#            x_shift = SearchAlgorithm.__scrap_shift(x_frame_prop, x_prop, n_pic)

            y_prop = y_frame_prop * divider_func(n_pic)
#            y_shift = SearchAlgorithm.__scrap_shift(y_frame_prop, y_prop, n_pic)

            x, y = 0, 0
            while y + y_prop < 1:
#                while (x + x_prop < 1) and not isclose(x + x_prop, 1, rel_tol=1e-07, abs_tol=0.0):
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
        if isinstance(img_prop, type(())):
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
    def __init__(self, model, algorithm: SearchAlgorithm):
        # TODO
        pass
