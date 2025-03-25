# Gesture-Controlled Servo Motor Using Arduino & OpenCV

## Overview
This project uses OpenCV and Arduino to control a servo motor using hand gestures detected via a webcam. It integrates Python-based gesture recognition with embedded system control, making it a practical application of computer vision and embedded electronics.

## Features
- Hand gesture detection using OpenCV and MediaPipe
- Real-time servo motor control via Arduino
- Serial communication between Python and Arduino
- Customizable gestures for different servo positions

## Components Used
- **Hardware:**
  - Arduino board
  - Servo motor
  - Webcam
  - Connecting wires
  
- **Software:**
  - Python (OpenCV, MediaPipe, PySerial)
  - Arduino IDE (C++ for motor control)

## Working Principle
1. The webcam captures hand gestures in real time.
2. OpenCV and MediaPipe process the video feed to recognize gestures.
3. The detected gesture is mapped to a servo movement command.
4. Python sends the command to Arduino via serial communication.
5. Arduino adjusts the servo motor accordingly.

## How to Run
1. Upload the Arduino sketch to your Arduino board.
2. Run the Python script on your computer.
3. Place your hand in front of the webcam and control the servo using gestures.

## Applications
- Robotics and automation
- Touchless control systems

