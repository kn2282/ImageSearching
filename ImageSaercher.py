from pip._internal.utils.misc import enum

class AlgorithmType(enum):
    HALF_IMAGES = 1
    QUARTER_IMAGES = 2
    HORIZONTAL = 3
    VERTICAL = 4


class SearchAlgorithm:
    def __init__(self, type: AlgorithmType, img_prop: float = 1, model_input_prop: float = 1, max_depth: int = 4):
        """

        :type max_depth: max depth of saerchimg inside picture.
         Bigger depth -> algorithm searches to smaller pice of picture
        """
        self.max_depth = max_depth
        self.model_input_prop = model_input_prop
        self.type = type
        self.img_prop = img_prop

        if img_prop > model_input_prop:
            self.__main_y_prop = 1.
            self.__main_x_prop = model_input_prop / img_prop
        else:
            self.__main_x_prop = 1.
            self.__main_y_prop = img_prop / model_input_prop

        if type == AlgorithmType.HALF_IMAGES:
            self.__no_pictures_in_depth = [ 2**i for i in range(1, max_depth+1)]
            self.__prop_divider_func = lambda x: 2/(x + 1)

class ImageSearcher:
    def __init__(self, model, algorithm: SearchAlgorithm):
        #TODO
        pass