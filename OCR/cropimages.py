import cv2
import numpy as np

from Compute import *

import keras


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged


class CropImages(object):
    def __init__(self, file_path) -> None:
        self.image = cv2.imread(file_path)

    def cropped_images(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = auto_canny(blurred)
        ret, thresh = cv2.threshold(edged, 127, 255, 0)
        img_dilate = cv2.dilate(
            thresh, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        )
        contours, _ = cv2.findContours(
            img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        filtered_contours = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w >= 10 and h >= 10 and w <= 70 and h <= 70:
                filtered_contours.append((x, y, w, h))

        filtered_contours = sorted(filtered_contours, key=lambda contour: contour[2])

        filtered_contours = sorted(filtered_contours, key=lambda contour: contour[1])

        return [
            (
                self.image[
                    coord[1] : coord[1] + coord[3], coord[0] : coord[0] + coord[2]
                ],
                coord,
            )
            for coord in filtered_contours
        ]


if __name__ == "__main__":
    file_path = (
        "/Users/manselmartins/Documents/PslayersInspirus/P-Sayers/OCR/Data/A4/1.jpg"
    )

    crop = CropImages(file_path)
    l = crop.cropped_images()
    # print(l[0][1])

    img_height = 75
    img_width = 50

    for i, imag in enumerate(l[:10]):
        cv2.imshow(f"cropped{i}", imag[0])

        #  send paths here
        # convert(path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
