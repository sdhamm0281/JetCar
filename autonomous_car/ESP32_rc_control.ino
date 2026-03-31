// ===== PIN SETUP =====
#define STEERING_PIN 18
#define ESC_PIN 19

// ===== PWM SETTINGS =====
#define PWM_FREQ 50          // 50Hz for servo/ESC
#define PWM_RESOLUTION 16    // 16-bit resolution

#define STEERING_CHANNEL 0
#define ESC_CHANNEL 1

// ===== PWM RANGE =====
#define PWM_MIN 3277    // ~1000us
#define PWM_MAX 6553    // ~2000us
#define PWM_NEUTRAL 4915 // ~1500us

// ===== FAILSAFE =====
unsigned long lastCommandTime = 0;
const int FAILSAFE_TIMEOUT = 500; // ms

// ===== CURRENT VALUES =====
int currentSteering = PWM_NEUTRAL;
int currentThrottle = PWM_NEUTRAL;

void setup() {
  Serial.begin(115200);

  // Setup PWM channels
  ledcSetup(STEERING_CHANNEL, PWM_FREQ, PWM_RESOLUTION);
  ledcAttachPin(STEERING_PIN, STEERING_CHANNEL);

  ledcSetup(ESC_CHANNEL, PWM_FREQ, PWM_RESOLUTION);
  ledcAttachPin(ESC_PIN, ESC_CHANNEL);

  // Initialize neutral
  ledcWrite(STEERING_CHANNEL, PWM_NEUTRAL);
  ledcWrite(ESC_CHANNEL, PWM_NEUTRAL);

  ledcWrite(ESC_CHANNEL, PWM_MAX);
  delay(2000);
  ledcWrite(ESC_CHANNEL, PWM_MIN);
  delay(2000);
  ledcWrite(ESC_CHANNEL, PWM_NEUTRAL);
  
  delay(2000); // ESC arm time
}

// ===== MAP FUNCTIONS =====
int mapSteering(int val) {
  // -100 to 100 → PWM
  return map(val, -100, 100, PWM_MIN, PWM_MAX);
}

int mapThrottle(int val) {
  // 0 to 100 → PWM (forward only)
  return map(val, 0, 100, PWM_NEUTRAL, PWM_MAX);
}

// ===== MAIN LOOP =====
void loop() {
  if (Serial.available()) {
    String msg = Serial.readStringUntil('\n');

    int sIndex = msg.indexOf('S');
    int tIndex = msg.indexOf('T');

    if (sIndex != -1 && tIndex != -1) {
      int steering = msg.substring(sIndex + 1, tIndex).toInt();
      int throttle = msg.substring(tIndex + 1).toInt();

      currentSteering = mapSteering(steering);
      currentThrottle = mapThrottle(throttle);

      ledcWrite(STEERING_CHANNEL, currentSteering);
      ledcWrite(ESC_CHANNEL, currentThrottle);

      lastCommandTime = millis();
    }
  }

  // ===== FAILSAFE =====
  if (millis() - lastCommandTime > FAILSAFE_TIMEOUT) {
    ledcWrite(ESC_CHANNEL, PWM_NEUTRAL); // stop motor
  }
}