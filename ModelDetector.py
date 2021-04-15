from PIL import Image
import tensorflow as tf


def image2table(im: Image.Image, im_size: (int, int)):
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


def index_highest(table):
    highest_v = max(table[0])
    for i in range(len(table[0])):
        if highest_v == table[0][i]:
            return i


class ModelDetector:
    def __init__(self, img_size: () = (20, 20), out_number: int = 2, layer_factors=None):
        if layer_factors is None:
            layer_factors = [1]
        layers = [tf.keras.layers.Flatten(input_shape=img_size)] + \
            [tf.keras.layers.Dense(int(img_size[0] * img_size[1] * i), activation='relu') for i in layer_factors] + \
            [tf.keras.layers.Dense(out_number, activation='sigmoid')]

        self.model = tf.keras.Sequential(layers)
        self.model.compile(
            optimizer='sgd',
            loss='binary_crossentropy',
            metrics=['binary_accuracy']
#            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
#            metrics=['accuracy']
        )
        self._images: [] = []
        self._accuracyImages: [] = []

        self._labels: [] = []
        self._accuracyLabels: [] = []

        self.__img_size = img_size
        pass

    def __load_single_image(self, image_name: "", label: int, images, labels):
        loading_image: Image.Image = Image.open(image_name)
        images.append(image2table(loading_image, self.__img_size))
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
        im = Image.open(img_name)
        predictions = self.model.predict([image2table(im, self.__img_size)])
        return predictions

    def save(self, path: str):
        self.model.save(path)
