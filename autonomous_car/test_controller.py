from control.controller import Controller
from utils.serial_comm import SerialComm
import time

serial_comm = SerialComm('/dev/ttyUSB0', 115200)
controller = Controller(serial_comm)

for t in range(0, 50, 5):
    print(f"Throttle: {t}")
    controller.drive(0, t)
    time.sleep(0.5)

controller.drive(0, 0)