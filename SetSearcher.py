from ImageSearcher import ImageSearcher, SearchAlgorithm, AlgorithmType


def SearchSet(photos_path, parameters_path, search_alg=None, max_depth=None, alg_type=None, confidence_level=None, sure_level=None):
    searcher = ImageSearcher.load(path=parameters_path, search_alg=search_alg, max_depth=max_depth, alg_type=alg_type, confidence_level=confidence_level)

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

    if sure_level is None:
        sure_level = min(confidence_level + 0.1, 0.95)
        sure_level = max(sure_level, confidence_level)

    for image in photos:
        _, confidence = searcher.searchImage(image)
        if confidence > sure_level:
            dir_with += [image]
        elif sure_level > confidence > confidence_level:
            dir_questionable += [image]
        else:
            dir_without += image

    return dir_with, dir_questionable, dir_without
