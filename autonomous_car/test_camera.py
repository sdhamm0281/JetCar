import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import cv2
from autonomous_car.sensors.camera import Camera

camera = Camera()

while True:
    frame = camera.get_frame()
    if frame is None:
        continue

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) == 27:
        break