import serial
import time

class SerialComm:
    def __init__(self, port='/dev/ttyUSB0', baud=115200):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)

    def send(self, steering, throttle):
        # Format: SXXXTYYY\n
        msg = f"S{int(steering)}T{int(throttle)}\n"
        self.ser.write(msg.encode())