#include <Servo.h>

Servo myServo;
int servoPin = 9;  // Connect your servo to pin 9
int angle = 0;

void setup() {
    Serial.begin(9600);
    myServo.attach(servoPin);
    myServo.write(90);  // Start at 90 degrees
}

void loop() {
    if (Serial.available() > 0) {
        angle = Serial.parseInt();  // Read the angle sent from Python
        angle = constrain(angle, 0, 180);  // Constrain the angle to avoid overdriving
        myServo.write(angle);
        Serial.println(angle);  // For debugging
    }
}
