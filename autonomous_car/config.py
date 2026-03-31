# ===== CONTROL =====
MAX_THROTTLE = 30
BASE_THROTTLE = 25
STEERING_GAIN = 0.12

# ===== SAFETY =====
OBSTACLE_DISTANCE_STOP = 500  # mm

# ===== LOOP =====
LOOP_HZ = 20

# ===== SERIAL =====
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 115200

# ===== CAMERA =====
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# ===== VISION (color-based line following) =====
LOWER_COLOR = (0, 0, 200)     # white line (HSV)
UPPER_COLOR = (180, 40, 255)

# ===== DEBUG =====
SHOW_CAMERA = True