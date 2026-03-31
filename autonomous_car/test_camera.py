import cv2
from sensors.camera import Camera

camera = Camera()

while True:
    frame = camera.get_frame()
    if frame is None:
        continue

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) == 27:
        break