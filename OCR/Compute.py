import tensorflow as tf
import keras

f = open("./map.txt", "r")

string = f.read()

mapArray = string.split("\n")
f.close()


model = keras.models.load_model("./hieroglyph_model")

# Check its architecture
# model.summary()


import numpy as np
from keras.preprocessing import image

img_height = 75
img_width = 50


def Compute(img):
    # img = image.load_img('../data/glyphdataset/Dataset/Automated/Preprocessed/3/030026_S29.png', target_size = (img_height, img_width))
    # img = image.load_img('../data/glyphdataset/Dataset/Automated/Preprocessed/3/030030_S29.png', target_size = (img_height, img_width))
    # img = image.load_img(
    #     "/Users/manselmartins/Downloads/test.png",
    #     target_size=(img_height, img_width),
    # )
    # img = image.load_img('../data/glyphdataset/Dataset/Automated/Preprocessed/3/030024_E34.png', target_size = (img_height, img_width))
    # img = image.load_img('../data/glyphdataset/Dataset/Automated/Preprocessed/3/030147_E34.png', target_size = (img_height, img_width))
    # img = image.load_img('../data/glyphdataset/Dataset/Automated/Preprocessed/3/030443_E34.png', target_size = (img_height, img_width))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    # gardiner = model.predict(img)

    # print(max(gardiner))

    # for i in range(len(img)):
    #     print("X=%s, Predicted=%s" % (img[i], gardiner[i]))

    # Xnew = [[...], [...]]
    ynew = model.predict(img)

    # for i in range(len(img)):
    #     print("X=%s, Predicted=%s" % (img[i], ynew[i]))

    classes = np.argmax(ynew, axis=1)
    print(classes)

    print(mapArray[classes[0]])

    return mapArray[classes[0]]

    # print(ynew)


img = image.load_img(
    "/Users/manselmartins/Downloads/test.png",
    target_size=(img_height, img_width),
)

print(Compute(img))
