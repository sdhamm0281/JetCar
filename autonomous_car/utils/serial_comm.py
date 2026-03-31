import serial
import time

class SerialComm:
    def __init__(self, port, baud):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)

    def send(self, steering, throttle):
        msg = f"S{int(steering)}T{int(throttle)}\n"
        self.ser.write(msg.encode())