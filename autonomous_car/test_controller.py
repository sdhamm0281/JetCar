import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from autonomous_car.control.controller import Controller
from autonomous_car.utils.serial_comm import SerialComm
import time

serial_comm = SerialComm('/dev/ttyUSB0', 115200)
controller = Controller(serial_comm)

for t in range(0, 50, 5):
    print(f"Throttle: {t}")
    controller.drive(0, t)
    time.sleep(0.5)

controller.drive(0, 0)