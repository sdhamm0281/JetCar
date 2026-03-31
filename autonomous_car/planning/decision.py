from autonomous_car.config import MAX_THROTTLE, BASE_THROTTLE, STEERING_GAIN, OBSTACLE_DISTANCE_STOP

class Decision:
    def compute(self, lane_center, frame_width, obstacle_distance):
        error = lane_center - (frame_width / 2)

        steering = -error * STEERING_GAIN

        if obstacle_distance < OBSTACLE_DISTANCE_STOP:
            throttle = 0
        else:
            throttle = min(BASE_THROTTLE, MAX_THROTTLE)

        return steering, throttle