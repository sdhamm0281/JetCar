import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from autonomous_car.utils.serial_comm import SerialComm
import time

ser = SerialComm('/dev/ttyUSB0', 115200)

print("Testing...")

ser.send(0, 0)
time.sleep(2)

ser.send(0, 20)
time.sleep(2)

ser.send(50, 20)
time.sleep(2)

ser.send(-50, 20)
time.sleep(2)

ser.send(0, 0)