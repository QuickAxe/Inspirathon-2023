import random
import cv2
import numpy as np
import imutils


def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged


img_path = "/test4435.jpg"
hiero = cv2.imread(img_path)
# hiero = cv2.resize(hiero, (500, 750), interpolation=cv2.INTER_LINEAR)
gray = cv2.cvtColor(hiero, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)


edged = auto_canny(blurred)
ret, thresh = cv2.threshold(edged, 127, 255, 0)
# img_dilate = cv2.dilate(thresh, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))  # Adjust the kernel size as needed
# contours, hierarchy = cv2.findContours(img_dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# # contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


# contours = sorted(contours, key = cv2.contourArea, reverse = True)
# for i in range(len(contours)):
#     contour = contours[i]

#     color = (20,218,30)
#     cv2.drawContours(hiero,[contour], -1, color, 3)

# boundRect = [None]*len(contours)
# for i, c in enumerate(contours):
#     contours_poly = cv2.approxPolyDP(c, 3, True)
#     boundRect[i] = cv2.boundingRect(contours_poly)

# for i in range(len(contours)):
#     cv2.rectangle(hiero, (int(boundRect[i][0]), int(boundRect[i][1])), (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), (0,0,0), 2)
img_dilate = cv2.dilate(
    thresh, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))

# Find contours in the dilated image
contours, _ = cv2.findContours(
    img_dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
filtered_contours = []
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w >= 30 and h >= 30:
        filtered_contours.append((x, y, w, h))


filtered_contours = sorted(filtered_contours,
                           key=lambda contour: contour[1])

n = len(filtered_contours)

# Draw bounding boxes around the contours on the original image
contour = filtered_contours[0]
cropped = hiero[contour[1]: contour[1] +
                contour[3], contour[0]:contour[0] + contour[2]]
for contour in filtered_contours:
    x, y, w, h = contour
    if (w == 50 and h == 50):
        colour = (0, 255, 0)
    elif (w >= 75 or h >= 50):
        colour = (255, 0, 0)
    else:
        colour = (255, 255, 255)
    cv2.rectangle(hiero, (contour[0], contour[1]),
                  (contour[0] + contour[2], contour[1] + contour[3]),
                  colour, 2)
cropped = cv2.resize(cropped, (50, 75), interpolation=cv2.INTER_LINEAR)
# Show the image with bounding boxes
# cv2.imshow("cropped", cropped)
cv2.imshow("Hiero", hiero)
# cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
