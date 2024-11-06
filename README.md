# Motor-Controlling
In this experiment we are controlling the servo motor using hand gestures.The main objective of this experiment is to demonstrate effective communication between Python code, Arduino, and a servo motor. We’ve utilized a range of powerful libraries for this task, including pyserial (for serial communication), opencv-python (for image processing), cvzone (to bridge Python with Arduino), mediapipe (for hand tracking), and numpy (for numerical operations).
This experiment employs a webcam to capture hand gestures, detects hand landmarks using Mediapipe, and calculates the distance between specific points (the thumb and index finger) to map and send motor control signals to the Arduino. The result is a responsive system that adjusts motor speed based on hand gestures.

