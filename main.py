import cv2
import mediapipe as mp
from cvzone.SerialModule import SerialObject

# Variables for the motor control
arduino = SerialObject("COM6")  # Replace with your correct COM port
x1 = y1 = x2 = y2 = 0

# Initialize camera and Mediapipe hands detector
webcam = cv2.VideoCapture(0)
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    _, image = webcam.read()
    frame_height, frame_width, _ = image.shape

    # Convert image to RGB for hand detection
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks

    # Check if any hands are detected
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark

            # Iterate through hand landmarks to get thumb and index finger positions
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index finger tip
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:  # Thumb tip
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    x2 = x
                    y2 = y

                    # Calculate the distance between the thumb and index finger
                    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

                    # Map distance to speed or angle value
                    # For example, map dist (0-200) to angle (0-180)
                    speed = int(min(max((dist / 200) * 180, 0), 180))
                    arduino.sendData([speed])

    # Display the image with hand landmarks
    cv2.imshow("Image", image)

    # Exit loop if 'ESC' is pressed
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release resources
webcam.release()
cv2.destroyAllWindows()
import serial

# Replace 'COM3' with your Arduino's port (e.g., 'COM4' on Windows or '/dev/ttyUSB0' on Linux/Mac)
arduino_port = "COM3"
baud_rate = 9600  # Make sure this matches the baud rate in your Arduino code

# Initialize the serial connection
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

print(f"Connected to {arduino_port} at {baud_rate} baud rate")

try:
    while True:
        # Read a line of data from the serial port
        data = ser.readline().decode('utf-8').strip()

        # Only print the data if it's not empty
        if data:
            print(f"Received: {data}")
except KeyboardInterrupt:
    print("Serial reading stopped.")
finally:
    # Close the serial connection when done
    ser.close()
    print("Serial connection closed.")