import cv2
import mediapipe as mp
import os

# Initialize Mediapipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Coordinates for Dr. Driving controls (change based on your device resolution)
ACCEL_X, ACCEL_Y = 900, 1600   # Right pedal
BRAKE_X, BRAKE_Y = 200, 1600   # Left pedal
LEFT_X, LEFT_Y = 200, 1200     # Left side steering
RIGHT_X, RIGHT_Y = 900, 1200   # Right side steering

# Open camera
cap = cv2.VideoCapture(0)

def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip for mirror effect
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Simple gesture logic
            # Tip landmarks: index (8), middle (12), ring (16), pinky (20), thumb (4)
            finger_tips = [8, 12, 16, 20]
            fingers = []

            for tip in finger_tips:
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    fingers.append(1)  # Finger up
                else:
                    fingers.append(0)  # Finger down
            
            # Check gestures
            if fingers == [0, 0, 0, 0]:
                cv2.putText(frame, "BRAKE", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                tap(BRAKE_X, BRAKE_Y)
            elif fingers == [1, 0, 0, 0]:
                cv2.putText(frame, "ACCELERATE", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                tap(ACCEL_X, ACCEL_Y)
            elif fingers == [1, 1, 0, 0]:
                cv2.putText(frame, "LEFT", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                tap(LEFT_X, LEFT_Y)
            elif fingers == [1, 1, 1, 0]:
                cv2.putText(frame, "RIGHT", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                tap(RIGHT_X, RIGHT_Y)

    cv2.imshow("Dr. Driving Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
