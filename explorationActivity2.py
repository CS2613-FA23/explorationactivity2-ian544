# Essential imports
import cv2
import numpy as np

# Initializes the camera
cam = cv2.VideoCapture(0)

while True:
    # Captures each frame from the camera using multiple assignment
    isReadSuccessful, frame = cam.read() 

    # Flips the frame horizontally because webcam is going to give it a mirrored image
    frame = cv2.flip(frame, 1)

    # Converts the frame to grayscale
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve accuracy for later processing
    blurredFrame = cv2.GaussianBlur(grayFrame, (5, 5), 0)

    # Uses the OpenCV built-in hand cascade classifier by sending the filepath of where its located in the library
    hand_cascade = cv2.CascadeClassifier('haarcascade_hand.xml')

    # Detects hands in the frame
    hands = hand_cascade.detectMultiScale(blurredFrame, 1.1, 5)

    # Draw rectangles around the detected hands
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Extract the region of interest (hand) for gesture recognition
        roi = blurredFrame[y:y + h, x:x + w]

        # Example: Check if the hand is in an open fist position and annotate the image apropriatley
        hand_area = w * h
        if hand_area > 5000:
            cv2.putText(frame, 'Open Fist', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display the resulting frame in a window
    cv2.imshow('Gesture Recognition', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()

    