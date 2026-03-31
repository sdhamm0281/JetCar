import time
import cv2

from sensors.camera import Camera
from sensors.lidar import Lidar
from perception.lane_detection import detect_lane_center
from planning.decision import Decision
from control.controller import Controller
from utils.serial_comm import SerialComm
from autonomous_car.config import LOOP_HZ, SERIAL_PORT, BAUD_RATE, SHOW_CAMERA

# ===== INIT =====
camera = Camera()
lidar = Lidar()
decision = Decision()

serial_comm = SerialComm(SERIAL_PORT, BAUD_RATE)
controller = Controller(serial_comm)

dt = 1.0 / LOOP_HZ

# ===== LOOP =====
while True:
    start = time.time()

    frame = camera.get_frame()
    if frame is None:
        continue

    lane_center, width = detect_lane_center(frame)
    distance = lidar.get_distance_ahead()

    steering, throttle = decision.compute(lane_center, width, distance)

    controller.drive(steering, throttle)

    print(f"Steering: {steering:.2f}, Throttle: {throttle:.2f}")

    if SHOW_CAMERA:
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == 27:
            break

    elapsed = time.time() - start
    time.sleep(max(0, dt - elapsed))