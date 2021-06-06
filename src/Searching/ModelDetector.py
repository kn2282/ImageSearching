from PIL import Image
import tensorflow as tf


def image2table(im: Image.Image, im_size: (int, int)) -> []:
    """
    Function used to parse image into neural network.
    (changing image into proper format)

    :param im: image being transforming to table.
    :param im_size: target table size.
    :return: table of :param im_size size.
    """
    im_resized: Image.Image = im.resize(im_size)
    table_image = []
    if isinstance(im_resized.getpixel((0, 0)), int):
        is_greyscaled = True
    else:
        is_greyscaled = False
    for i in range(im_size[0]):
        table_image.append([])
        for j in range(im_size[1]):
            if is_greyscaled:
                pixel = im_resized.getpixel((i, j)) / 255.0
            else:
                pixel = sum(im_resized.getpixel((i, j))) / (3 * 255.0)
            table_image[i].append(pixel)
        pass
    return table_image





class ModelDetector:
    """
    Class used to manage neural network:
    train, test, save and predict answers.
    """
    def __init__(self, img_size: () = (20, 20), layer_factors=None, load_model=None):
        """
        Model Detector can be initiated for new neural network (load_model is None)
        or can load existing one (load_model is pair of (path_to_model, model_size)).

        :param img_size: size of input into neural network.
        :param layer_factors: sizes of next layers in neural network
            (must be given in fractals and will be multiply by size of input).
        :param load_model: pair of (path_to_model, model_size) or None if creating new one.
        """
        if load_model is not None:
            self.model = tf.keras.models.load_model(load_model[0])
            self._img_size = load_model[1]
        else:
            if layer_factors is None:
                layer_factors = [1]
            layers = [tf.keras.layers.Flatten(input_shape=img_size)] + \
                [tf.keras.layers.Dense(int(img_size[0] * img_size[1] * i), activation='relu') for i in layer_factors] + \
                [tf.keras.layers.Dense(1, activation='sigmoid')]

            self.model = tf.keras.Sequential(layers)
            self.model.compile(
                optimizer='sgd',
                loss='binary_crossentropy',
                metrics=['binary_accuracy']
            )
            self._img_size = img_size

        self._images: [] = []
        self._accuracyImages: [] = []

        self._labels: [] = []
        self._accuracyLabels: [] = []
        pass

    def __load_single_image(self, image_name: "", label: int, images, labels):
        loading_image: Image.Image = Image.open(image_name)
        images.append(image2table(loading_image, self._img_size))
        labels.append(label)

    def __load_images(self, image_label_pairs, images, labels):
        for pair in image_label_pairs:
            self.__load_single_image(pair[0], pair[1], images, labels)

    def load_train_images(self, image_label_pairs: (str, int)):
        self.__load_images(image_label_pairs, self._images, self._labels)

    def load_accuracy_images(self, image_label_pairs):
        self.__load_images(image_label_pairs, self._accuracyImages, self._accuracyLabels)

    def train(self, epochs: int = 25):
        self.model.fit(self._images, self._labels, epochs=epochs)

    def check_accuracy(self):
        test_loss, test_acc = self.model.evaluate(self._accuracyImages, self._accuracyLabels, verbose=2)
        return test_acc

    def predict(self, img_name: ""):
        if isinstance(img_name, (type(''), type(""))):
            im = Image.open(img_name)
        elif isinstance(img_name, Image.Image):
            im = img_name
        else:
            raise TypeError(f"invalid type {type(img_name)} : must be path to image or image")
        predictions = self.model.predict([image2table(im, self._img_size)])
        return predictions[0][0]

    def save(self, path: str):
        self.model.save(path)
