import cv2
import numpy as np

def detect_lane_center(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    edges = cv2.Canny(blur, 50, 150)

    height, width = edges.shape
    roi = edges[int(height*0.6):height, :]

    histogram = np.sum(roi, axis=0)
    center = np.argmax(histogram)

    return center, width