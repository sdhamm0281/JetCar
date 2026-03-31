class Controller:
    def __init__(self, serial_comm):
        self.serial = serial_comm
        self.last_throttle = 0
        self.max_delta = 5

    def drive(self, steering, throttle):
        steering = max(-100, min(100, steering))
        throttle = max(0, min(100, throttle))

        # Smooth throttle
        delta = throttle - self.last_throttle
        if abs(delta) > self.max_delta:
            throttle = self.last_throttle + self.max_delta * (1 if delta > 0 else -1)

        self.last_throttle = throttle

        self.serial.send(steering, throttle)