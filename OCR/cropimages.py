import cv2
import numpy as np


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
        with cv2.imread(file_path) as f:
            self.image = f

    def cropped_images():
        gray = cv2.cvtColor(hiero, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        edged = auto_canny(blurred)
        ret, thresh = cv2.threshold(edged, 127, 255, 0)
        img_dilate = cv2.dilate(
            thresh, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
        contours, _ = cv2.findContours(
            img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        filtered_contours = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w >= 10 and h >= 10:
                filtered_contours.append((x, y, w, h))

        filtered_contours = sorted(filtered_contours,
                                   key=lambda contour: contour[2])

        filtered_contours = sorted(filtered_contours,
                                   key=lambda contour: contour[1])
        return ((self.image[coord[0]:coord[1], coord[2]:coord[4]], coord) for coord in filtered_contours)


if __name__ == "__main__":
    file_path = "/data/Coding/INSPIRATHON2023/Dataset/Pictures/egyptianTexts5.jpg"

    crop = CropImages(file_path)
    l = crop.cropped_images()
