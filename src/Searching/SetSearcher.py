from .ImageSearcher import ImageSearcher
import os
import json


def SearchSet(photos_path, parameters_path, max_depth=None, alg_type=None, confidence_level=None):
    """
    Function that takes photos and parameters as input and returns two arrays of photo paths. One contains
    selected images by algorithm and the second contains the rest.
    :param photos_path: array of photo paths for algorithm
    :param parameters_path: parameters for the load function
    :param max_depth: variable passed to ImageSearcher, the bigger the more precisely an image is searched
    :param alg_type: HALF_IMAGES or QUARTER_IMAGES
    :param confidence_level: acceptance rate of an image
    :return: array of selected and array of not selected images (arrays of absolute paths)
    """
    searcher = ImageSearcher.load(path=parameters_path, max_depth=max_depth, alg_type=alg_type, confidence_level=confidence_level)

    dir_with = []
    dir_without = []

    photos = []
    for (dir_path, dir_names, filenames) in os.walk(photos_path):
        for file in filenames:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                photos.append(os.path.join(dir_path, file))

    if confidence_level is None:
        with open(parameters_path, "r") as json_file:
            confidence_level = json.load(json_file)["confidence_level"]

    for i, image in enumerate(photos):
        print(image)
        _, confidence = searcher.searchImage(image)

        if confidence > confidence_level:
            dir_with += [image]
        else:
            dir_without += [image]

    return dir_with, dir_without
