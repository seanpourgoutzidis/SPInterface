# Computer Vision
import cv2
import mediapipe as mp
import pyautogui

# General Libraries
import time
from enum import Enum
from models import Hand, State, Coordinate
from commands import Commands, CommandTypes

# Initialize System State (Object that represents hands)
leftHand = Hand(Coordinate(0,0), Coordinate(0,0), Coordinate(0,0), Coordinate(0,0), Coordinate(0,0))
rightHand = Hand(Coordinate(0,0), Coordinate(0,0), Coordinate(0,0), Coordinate(0,0), Coordinate(0,0))
STATE = State(leftHand, rightHand, False, False, False, False, False, 0, False)

# Initialize hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

# Get screen resolution
screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)

def getUserInput():

    global STATE

    while cap.isOpened():

        ret,frame = cap.read()

        # Flip the frame horizontally
        frame = cv2.flip(frame, 1)

        # Convert to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)
     
        # Check if hand landmarks are available
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:

                hand = results.multi_handedness[results.multi_hand_landmarks.index(landmarks)].classification[0].label

                mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

                if hand == "Left":
                    # Get tips of fingers
                    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                    # Update State
                    STATE.left.thumb.set(int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height))
                    STATE.left.index.set(int(index_tip.x * screen_width), int(index_tip.y * screen_height))
                    STATE.left.middle.set(int(middle_tip.x * screen_width), int(middle_tip.y * screen_height))
                    STATE.left.ring.set(int(ring_tip.x * screen_width), int(ring_tip.y * screen_height))
                    STATE.left.pinky.set(int(pinky_tip.x * screen_width), int(pinky_tip.y * screen_height))


                elif hand == "Right":
                    # Get tips of fingers
                    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

                    # Update State
                    STATE.right.thumb.set(int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height))
                    STATE.right.index.set(int(index_tip.x * screen_width), int(index_tip.y * screen_height))
                    STATE.right.middle.set(int(middle_tip.x * screen_width), int(middle_tip.y * screen_height))
                    STATE.right.ring.set(int(ring_tip.x * screen_width), int(ring_tip.y * screen_height))
                    STATE.right.pinky.set(int(pinky_tip.x * screen_width), int(pinky_tip.y * screen_height))


                # if (STATE.AreThumbsTouching()): # Exit App
                #     Commands[CommandTypes.THUMBS].execute(STATE)
                if (STATE.ArePinkiesTouching()):
                    Commands[CommandTypes.PINKIES].execute(STATE)

                if (STATE.AreIndexesTouching()): # Toggle Tracking
                    Commands[CommandTypes.INDEXES].execute(STATE)
                    break

                if (STATE.AreMiddlesTouching()):
                    Commands[CommandTypes.MIDDLES].execute(STATE)

                if (not(STATE.isTracking)):
                    continue

                if (STATE.left.IsPinchGesture()):
                    Commands[CommandTypes.LEFTPINCH].execute(STATE)

                if (STATE.right.IsPinchGesture()):
                    Commands[CommandTypes.RIGHTPINCH].execute(STATE)
                

                if (STATE.left.IsIndexTouchingThumb() and not(STATE.left.IsPinchGesture())): # Click mouse or zoom in if we are zooming or scroll down if we are scrolling
                    Commands[CommandTypes.LEFTINDEX].execute(STATE)
                elif (STATE.left.IsMiddleTouchingThumb() and not(STATE.left.IsPinchGesture())): # Press Tab or zoom out if we are zooming or scroll up if we are scrolling
                    Commands[CommandTypes.LEFTMIDDLE].execute(STATE)
                elif (STATE.left.IsRingTouchingThumb()): # Press Enter
                    Commands[CommandTypes.LEFTRING].execute(STATE)
                elif (STATE.left.IsPinkyTouchingThumb()): # Press Esc
                    Commands[CommandTypes.LEFTPINKY].execute(STATE)

                # Handle Cursor Function
                if (STATE.right.IsIndexTouchingThumb() and not(STATE.isCursor) and not(STATE.right.IsPinchGesture())):
                    print('Cursor On')
                    STATE.isCursor = True
                elif (not(STATE.right.IsIndexTouchingThumb()) and STATE.isCursor):
                    print('Cursor Off')
                    STATE.isCursor = False
                elif(STATE.right.IsIndexTouchingThumb() and STATE.isCursor and not(STATE.right.IsPinchGesture())):
                    pyautogui.moveTo(STATE.right.index.x, STATE.right.index.y, duration=0.1)

                # Handle Zoom Function
                if (STATE.right.IsMiddleTouchingThumb() and not(STATE.isZooming) and not(STATE.isScrolling) and not(STATE.isShifting) and not(STATE.right.IsPinchGesture())):
                    print('Zoom on')
                    STATE.isZooming = True
                elif (not(STATE.right.IsMiddleTouchingThumb()) and STATE.isZooming):
                    print('Zoom off')
                    STATE.isZooming = False

                # Handle Scroll Function
                if (STATE.right.IsRingTouchingThumb() and not(STATE.isScrolling) and not(STATE.isZooming) and not(STATE.isShifting)):
                    print('Scroll on')
                    STATE.isScrolling = True
                elif (not(STATE.right.IsRingTouchingThumb()) and STATE.isScrolling):
                    print('Scroll off')
                    STATE.isScrolling = False

                # Handle Shift
                if (STATE.right.IsPinkyTouchingThumb() and not(STATE.isShifting) and not(STATE.isZooming) and not(STATE.isScrolling)):
                    print('Shift on')
                    STATE.isShifting = True
                elif (not(STATE.right.IsPinkyTouchingThumb()) and STATE.isShifting):
                    print('Shift off')
                    STATE.isShifting = False


        if STATE.debugMode:
            cv2.imshow("Gesture Recognition", frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    getUserInput()





                