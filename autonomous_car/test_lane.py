import cv2
from sensors.camera import Camera
from perception.lane_detection import detect_lane_center

camera = Camera()

while True:
    frame = camera.get_frame()
    if frame is None:
        continue

    center, width = detect_lane_center(frame)

    # Draw center line
    cv2.line(frame, (center, 0), (center, frame.shape[0]), (0,255,0), 2)
    cv2.line(frame, (width//2, 0), (width//2, frame.shape[0]), (0,0,255), 2)

    cv2.imshow("Lane Test", frame)

    print(f"Center: {center}, Error: {center - width//2}")

    if cv2.waitKey(1) == 27:
        break