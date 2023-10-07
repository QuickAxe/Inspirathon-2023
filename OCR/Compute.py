import tensorflow as tf
import keras
import os


mapArray = [
    "A55",
    "Aa15",
    "Aa26",
    "Aa27",
    "Aa28",
    "D1",
    "D10",
    "D156",
    "D19",
    "D2",
    "D21",
    "D28",
    "D34",
    "D35",
    "D36",
    "D39",
    "D4",
    "D46",
    "D52",
    "D53",
    "D54",
    "D56",
    "D58",
    "D60",
    "D62",
    "E1",
    "E17",
    "E23",
    "E34",
    "E9",
    "F12",
    "F13",
    "F16",
    "F18",
    "F21",
    "F22",
    "F23",
    "F26",
    "F29",
    "F30",
    "F31",
    "F32",
    "F34",
    "F35",
    "F4",
    "F40",
    "F9",
    "G1",
    "G10",
    "G14",
    "G17",
    "G21",
    "G25",
    "G26",
    "G29",
    "G35",
    "G36",
    "G37",
    "G39",
    "G4",
    "G40",
    "G43",
    "G5",
    "G50",
    "G7",
    "H6",
    "I10",
    "I5",
    "I9",
    "L1",
    "M1",
    "M12",
    "M16",
    "M17",
    "M18",
    "M195",
    "M20",
    "M23",
    "M26",
    "M29",
    "M3",
    "M4",
    "M40",
    "M41",
    "M42",
    "M44",
    "M8",
    "N1",
    "N14",
    "N16",
    "N17",
    "N18",
    "N19",
    "N2",
    "N24",
    "N25",
    "N26",
    "N29",
    "N30",
    "N31",
    "N35",
    "N36",
    "N37",
    "N41",
    "N5",
    "O1",
    "O11",
    "O28",
    "O29",
    "O31",
    "O34",
    "O4",
    "O49",
    "O50",
    "O51",
    "P1",
    "P13",
    "P6",
    "P8",
    "P98",
    "Q1",
    "Q3",
    "Q7",
    "R4",
    "R8",
    "S24",
    "S28",
    "S29",
    "S34",
    "S42",
    "T14",
    "T20",
    "T21",
    "T22",
    "T28",
    "T30",
    "U1",
    "U15",
    "U28",
    "U33",
    "U35",
    "U7",
    "UNKNOWN",
    "V13",
    "V16",
    "V22",
    "V24",
    "V25",
    "V28",
    "V30",
    "V31",
    "V4",
    "V6",
    "V7",
    "W11",
    "W14",
    "W15",
    "W18",
    "W19",
    "W22",
    "W24",
    "W25",
    "X1",
    "X6",
    "X8",
    "Y1",
    "Y2",
    "Y3",
    "Y5",
    "Z1",
    "Z11",
    "Z7",
    "",
    "",
]

import pathlib

rootPath = pathlib.Path().resolve()

model = keras.models.load_model(str(rootPath) + "/OCR" + "/hieroglyph_model")

# Check its architecture
# model.summary()


import numpy as np
from keras.preprocessing import image

img_height = 75
img_width = 50


def convert(img):
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

print(convert(img))
