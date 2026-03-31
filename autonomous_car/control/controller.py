class Controller:
    def __init__(self, serial_comm):
        self.serial = serial_comm

    def drive(self, steering, throttle):
        # Clamp values
        steering = max(-100, min(100, steering))
        throttle = max(0, min(100, throttle))

        self.serial.send(steering, throttle)