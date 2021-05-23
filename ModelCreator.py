# model = ModelDetector((70, 70), layer_factors=[0.7])
    #
    # train_images = []
    #
    # dir_with = "dataset/Cars/just_cars/"
    # for file in os.listdir(dir_with)[:-50]:
    #     train_images.append((dir_with + file, 1.))
    #
    # dir_without = "dataset/randoms/no_cars_and_faces/"
    # for file in os.listdir(dir_without)[:-80]:
    #     train_images.append((dir_without + file, 0.))
    #
    # model.load_train_images(train_images)
    #
    # test_images = []
    #
    # for file in os.listdir(dir_with)[-50:]:
    #     test_images.append((dir_with + file, 1.))
    #
    # for file in os.listdir(dir_without)[-80:]:
    #     test_images.append((dir_without + file, 0.))
    #
    # model.load_accuracy_images(test_images)
    #
    # model.train(epochs=10)
    # model.check_accuracy()
    #
    # print(model.predict("dataset/faces_dataset/65000/65984.png"))
    # print(model.predict("dataset/faces_dataset/65000/65992.png"))
    # print(model.predict("dataset/faces_dataset/65000/65996.png"))
    # print(model.predict("dataset/randoms/no_cars_and_faces/000000070048.jpg"))
    # print(model.predict("dataset/randoms/no_cars_and_faces/000000037751.jpg"))
    # print(model.predict("dataset/randoms/no_cars_and_faces/000000043581.jpg"))
    #
    # search_alg = SearchAlgorithm(
    #     AlgorithmType.HALF_IMAGES,
    #     1,
    #     4
    # )
    #
    # searcher = ImageSearcher(model, search_alg, 0.92, 'samochody')
    #
    # searcher.save()

    # load_searcher = ImageSearcher.load("models/twarze_parameters.json")

#    print(load_searcher.searchImage("photos/cat.jpg", search_all=True))
#    print(load_searcher.searchImage("photos/3.jpg", search_all=True))