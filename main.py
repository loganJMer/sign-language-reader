import cv2, sys, time
import mediapipe as mp
import keras
import numpy as np
import pandas as pd
from autocorrect import Speller

OUTPUTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', "H", 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ' ', '.']

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

    collect_data = input("Do you want to collect data? (y/n): ").lower() == 'y'
    label = OUTPUTS.index(input("Enter label for collected data: ")) if collect_data else None

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
                landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
                if collect_data and len(landmarks) == 21:
                    # Get relative positions and save to file
                    relative_landmarks = getRelativePositions(landmarks)
                    saveLandmarksToFile(relative_landmarks, label)


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

    if collect_data:
        trainModel()

def getRelativePositions(landmarks):
    wrist = landmarks[0]
    relatives = []
    for i in range(1, 21):
        relatives.append([landmarks[i][0] - wrist[0], landmarks[i][1] - wrist[1]])
    return relatives

def saveLandmarksToFile(landmarks, label, filename='data.csv'):
    # Convert label to a list before concatenation
    flat_landmarks = [coord for landmark in landmarks for coord in landmark[:2]]  # Use only x and y
    flat_landmarks.append(label)
    with open(filename, 'a') as f:
        np.savetxt(f, flat_landmarks, delimiter=",")  # Ensure it's a 1D array for saving


def trainModel():
    
    data = pd.read_csv('data.csv', )
    
    X = data.iloc[:,:-1].values
    Y = data.iloc[:,-1].values
    
    
    model = keras.models.Sequential([
        keras.layers.Dense(64, activation='relu', input_shape=(40,)),
        keras.layers.Dense(32, activation='relu'),
        keras.layers.Dense(38, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, epochs=10, validation_split=0.2)

    model.save('signModel.h5')

if __name__ == "__main__":
    main()
