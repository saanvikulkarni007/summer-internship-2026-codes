// 4-Lane Traffic Signal Controller
// Board: ESP32 DevKit V1  |  Wokwi compatible

// ── Pin definitions ──────────────────────────────────────────
#define NORTH_RED    2
#define NORTH_YELLOW 4
#define NORTH_GREEN  5

#define SOUTH_RED    18
#define SOUTH_YELLOW 19
#define SOUTH_GREEN  21

#define EAST_RED     22
#define EAST_YELLOW  23
#define EAST_GREEN   25

#define WEST_RED     26
#define WEST_YELLOW  27
#define WEST_GREEN   32

// ── Timing ────────────────────────────────────────────────────
#define GREEN_TIME  5000
#define YELLOW_TIME 2000

// ── Helper ────────────────────────────────────────────────────
void setSignal(int r, int y, int g, bool red, bool yellow, bool green) {
  digitalWrite(r, red    ? HIGH : LOW);
  digitalWrite(y, yellow ? HIGH : LOW);
  digitalWrite(g, green  ? HIGH : LOW);
}

void allRed() {
  setSignal(NORTH_RED, NORTH_YELLOW, NORTH_GREEN, true, false, false);
  setSignal(SOUTH_RED, SOUTH_YELLOW, SOUTH_GREEN, true, false, false);
  setSignal(EAST_RED,  EAST_YELLOW,  EAST_GREEN,  true, false, false);
  setSignal(WEST_RED,  WEST_YELLOW,  WEST_GREEN,  true, false, false);
}

// ── Phases ────────────────────────────────────────────────────
void phase_NS_Green() {
  Serial.println("[PHASE 1] N/S GREEN | E/W RED");
  setSignal(NORTH_RED, NORTH_YELLOW, NORTH_GREEN, false, false, true);
  setSignal(SOUTH_RED, SOUTH_YELLOW, SOUTH_GREEN, false, false, true);
  setSignal(EAST_RED,  EAST_YELLOW,  EAST_GREEN,  true,  false, false);
  setSignal(WEST_RED,  WEST_YELLOW,  WEST_GREEN,  true,  false, false);
  delay(GREEN_TIME);
}

void phase_NS_Yellow() {
  Serial.println("[PHASE 2] N/S YELLOW | E/W RED");
  setSignal(NORTH_RED, NORTH_YELLOW, NORTH_GREEN, false, true, false);
  setSignal(SOUTH_RED, SOUTH_YELLOW, SOUTH_GREEN, false, true, false);
  setSignal(EAST_RED,  EAST_YELLOW,  EAST_GREEN,  true,  false, false);
  setSignal(WEST_RED,  WEST_YELLOW,  WEST_GREEN,  true,  false, false);
  delay(YELLOW_TIME);
}

void phase_EW_Green() {
  Serial.println("[PHASE 3] E/W GREEN | N/S RED");
  setSignal(NORTH_RED, NORTH_YELLOW, NORTH_GREEN, true,  false, false);
  setSignal(SOUTH_RED, SOUTH_YELLOW, SOUTH_GREEN, true,  false, false);
  setSignal(EAST_RED,  EAST_YELLOW,  EAST_GREEN,  false, false, true);
  setSignal(WEST_RED,  WEST_YELLOW,  WEST_GREEN,  false, false, true);
  delay(GREEN_TIME);
}

void phase_EW_Yellow() {
  Serial.println("[PHASE 4] E/W YELLOW | N/S RED");
  setSignal(NORTH_RED, NORTH_YELLOW, NORTH_GREEN, true,  false, false);
  setSignal(SOUTH_RED, SOUTH_YELLOW, SOUTH_GREEN, true,  false, false);
  setSignal(EAST_RED,  EAST_YELLOW,  EAST_GREEN,  false, true, false);
  setSignal(WEST_RED,  WEST_YELLOW,  WEST_GREEN,  false, true, false);
  delay(YELLOW_TIME);
}

// ── Setup ─────────────────────────────────────────────────────
void setup() {
  Serial.begin(115200);
  int pins[] = {
    NORTH_RED, NORTH_YELLOW, NORTH_GREEN,
    SOUTH_RED, SOUTH_YELLOW, SOUTH_GREEN,
    EAST_RED,  EAST_YELLOW,  EAST_GREEN,
    WEST_RED,  WEST_YELLOW,  WEST_GREEN
  };
  for (int p : pins) { pinMode(p, OUTPUT); digitalWrite(p, LOW); }
  allRed();
  delay(1000);
}

// ── Loop ──────────────────────────────────────────────────────
void loop() {
  phase_NS_Green();
  phase_NS_Yellow();
  phase_EW_Green();
  phase_EW_Yellow();
}
