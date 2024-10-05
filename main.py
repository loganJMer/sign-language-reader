import cv2, sys, time
import mediapipe as mp
import tensorflow
from autocorrect import Speller
from manualLetterFind import find_letter


def main():
    feed = cv2.VideoCapture(0)
    if not feed.isOpened:
        print("Please ensure camera connection")
        exit()

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    lastLet = None
    lastCheck = 'A'
    diffCount = 0
    count = 0
    zCount = 0
    translation = ""
    time.sleep(1)
    left = True if input("If left hand type L:") == 'L' else False


    while True:
        ret, frame = feed.read()

        if not ret: break
        
        frame = cv2.flip(frame, 1) if left else frame
        # Convert the BGR image to RGB
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        landmarks = []
        # Process the frame with Mediapipe
        results = hands.process(rgb_image)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # mp.solutions.drawing_utils.draw_landmarks(
                #     frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = [(lm.x, lm.y, lm.z) for lm in hand_landmarks.landmark]

        letter = find_letter(landmarks)

        if letter and letter == lastCheck:
            count += 1
            if letter == lastLet:
                diffCount = 0
            if count == 5:
                if letter in ('D', 'Z'):
                    if letter == 'D':
                        if lastLet == 'Z' and zCount == 1:
                            zCount = 2
                        else:
                            translation += letter
                        lastLet = 'D'
                    else:
                        if lastLet == 'D':
                            if zCount == 0:
                                zCount = 1
                                lastLet = 'Z'
                            elif zCount == 2:
                                zCount = 0
                                lastLet = 'Z'
                                translation = translation[0:-1] + letter
                else:
                    if letter == 'J':
                        if lastLet == 'I':
                            translation = translation[0:-1] + 'J'
                            lastLet = 'J'
                    elif letter != lastLet:
                        translation += letter
                        lastLet = letter
        else:
            if letter != lastLet:
                diffCount += 1
                if diffCount == 5:
                    lastLet = None
            lastCheck = letter
            count = 1

        cv2.imshow('Hand Tracking', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Pre Spell-Check: " + translation.capitalize())
            print("Post Spell-Check: " + Speller()(translation.capitalize()))
            break
        

    feed.release()
    cv2.destroyAllWindows()

    if getattr(sys, 'frozen', False):
        input("Press Enter to exit...")


if __name__ == "__main__":
    main()
