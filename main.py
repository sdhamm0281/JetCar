from config import LOOP_HZ, SERIAL_PORT, BAUD_RATE, SHOW_CAMERA
import time
import cv2

serial_comm = SerialComm(SERIAL_PORT, BAUD_RATE)

dt = 1.0 / LOOP_HZ

while True:
    start = time.time()

    frame = camera.get_frame()
    if frame is None:
        continue

    lane_center, width = detect_lane_center(frame)
    distance = lidar.get_distance_ahead()

    steering, throttle = decision.compute(lane_center, width, distance)
    controller.drive(steering, throttle)

    if SHOW_CAMERA:
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break

    elapsed = time.time() - start
    time.sleep(max(0, dt - elapsed))