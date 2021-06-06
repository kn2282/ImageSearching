

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
    def __init__(self, alg_type: AlgorithmType, model_input_prop: float = 1, max_depth: int = 4):
        """

        :alg_type max_depth: max depth of searching inside picture.
         Bigger depth -> algorithm searches to smaller pace of picture
        """

        self.max_depth = max_depth
        self.model_input_prop = model_input_prop
        self.type = alg_type

        self.__n_pictures_in_depth = alg_type['n_pictures_in_depth'](max_depth)
        self.__prop_divider_func = alg_type['prop_divider_func']
        self.__pic_shift = alg_type['pic_shift']

    @staticmethod
    def __generator(x_frame_prop, y_frame_prop, n_pictures_in_depth, divider_func, pic_shift, max_depth):
        """
        Main search algorithm

        :param y_frame_prop, x_frame_prop: proportions of how much each axis of window was resized
                to adjust his edge to proportions of the picture
        :param n_pictures_in_depth: list of number of pictures in each depth.
        :param divider_func: function which tells how much smaller should be cropped window for number of pictures in row.
        :param pic_shift: parameter telling how much shift next cropped window.
                (for eg. 1/2 -> for half of length of previous picture)
        :param max_depth: parameter telling how much depths you have.
        :return: generator giving next positions ((x1, x2), (y1, y2)) were you should seek for model. (given in fractals)
        """

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
        Function returning generator activated with proper parameters.

        :param img_prop: proportions of searched image x to y (width to height)
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
