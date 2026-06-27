int ldrPin = A0;
int ledPin = 9;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int ldrValue = analogRead(ldrPin);
  int brightness = map(ldrValue, 0, 1023, 0, 255);
  analogWrite(ledPin, brightness);

  Serial.print("LDR: ");
  Serial.print(ldrValue);
  Serial.print(" | Brightness: ");
  Serial.println(brightness);

  delay(100);
}