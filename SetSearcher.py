from ImageSearcher import ImageSearcher, SearchAlgorithm, AlgorithmType


def SearchSet(image_set, parameters_path, dir_name='', search_alg=None, max_depth=None, alg_type=None, confidence_level=None):
    searcher = ImageSearcher.load(path=parameters_path, search_alg=search_alg, max_depth=max_depth, alg_type=None, confidence_level=None)

    dir_with = []
    dir_without = []
    for image in image_set:
        if searcher.searchImage(dir_name+image):
            dir_with += image
        else:
            dir_without += image

    return dir_with, dir_without
