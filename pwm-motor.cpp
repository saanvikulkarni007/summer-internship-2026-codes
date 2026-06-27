// PWM Motor Speed Control using Potentiometer and L293D
// Tinkercad Simulation

int potPin = A0;      // Potentiometer middle (wiper) pin
int motorPin = 9;     // PWM pin connected to Enable 1&2 of L293D
int in1Pin = 8;       // IN1 pin of L293D - controls direction

int potValue = 0;     // Raw potentiometer reading (0 to 1023)
int motorSpeed = 0;   // Mapped PWM value (0 to 255)

void setup() {
  pinMode(motorPin, OUTPUT);  // Enable pin as output
  pinMode(in1Pin, OUTPUT);    // IN1 pin as output
  
  digitalWrite(in1Pin, HIGH); // Set IN1 HIGH for forward direction
  
  Serial.begin(9600);         // Start serial monitor
  Serial.println("PWM Motor Speed Control Started");
}

void loop() {
  potValue = analogRead(potPin);               // Read potentiometer (0–1023)
  motorSpeed = map(potValue, 0, 1023, 0, 255); // Scale to PWM range (0–255)
  
  analogWrite(motorPin, motorSpeed);           // Send PWM to L293D Enable pin
  
  // Print values to Serial Monitor
  Serial.print("Potentiometer: ");
  Serial.print(potValue);
  Serial.print(" | Motor Speed (PWM): ");
  Serial.print(motorSpeed);
  Serial.print(" | Duty Cycle: ");
  Serial.print(map(motorSpeed, 0, 255, 0, 100));
  Serial.println("%");
  
  delay(200); // Small delay for stable reading
}