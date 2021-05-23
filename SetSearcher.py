from ImageSearcher import ImageSearcher, SearchAlgorithm, AlgorithmType
import os, json

def SearchSet(photos_path, parameters_path, max_depth=None, alg_type=None, confidence_level=None):
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

    for image in photos:
        _, confidence = searcher.searchImage(image)
        print(image)
        if confidence > confidence_level:
            dir_with += [image]
        else:
            dir_without += [image]

    return dir_with, dir_without
