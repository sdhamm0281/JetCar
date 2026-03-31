import cv2
import numpy as np
from config import LOWER_COLOR, UPPER_COLOR

def detect_lane_center(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)

    height, width = mask.shape

    # Focus on bottom 40% of image
    roi = mask[int(height * 0.6):height, :]

    M = cv2.moments(roi)

    if M["m00"] == 0:
        return width // 2, width  # default center if no line found

    cx = int(M["m10"] / M["m00"])

    return cx, width