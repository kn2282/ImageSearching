from pip._internal.utils.misc import enum

class AlgorithmType(enum):
    smallImages = 1
    bigImages = 2
    #TODO

class SearchAlgorithm:
    def __init__(self, type: AlgorithmType, img_proportions: float = 1):
        #TODO
        pass

class ImageSearcher:
    def __init__(self, model, algorithm: SearchAlgorithm):
        #TODO
        pass