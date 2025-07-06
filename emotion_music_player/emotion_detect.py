import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
#import pygame
#from spotify_player import play_emotion_track
from youtube_player import play_youtube_audio



# Suppress TensorFlow GPU and compile warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Load emotion detection model
model = load_model("emotion_model.h5", compile=False)
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Initialize pygame for music playback
#pygame.mixer.init()

# Define emotion-based music folder mapping (local .mp3 or .wav files)
music_paths = {
    "Angry": "music/angry/",
    "Disgust": "music/neutral/",
    "Fear": "music/neutral/",
    "Happy": "music/happy/",
    "Sad": "music/sad/",
    "Surprise": "music/happy/",
    "Neutral": "music/neutral/"
}

# Keep track of last played emotion to avoid rapid switching
last_emotion = None

# def play_song(emotion):
#     global last_emotion
#     if emotion == last_emotion:
#         return
#     last_emotion = emotion
#     folder = music_paths.get(emotion, "music/neutral/")
#     if not os.path.exists(folder):
#         print(f"No music folder for {emotion}")
#         return
#     songs = [f for f in os.listdir(folder) if f.endswith((".mp3", ".wav"))]
#     if songs:
#         pygame.mixer.music.load(os.path.join(folder, songs[0]))
#         pygame.mixer.music.play()
#     else:
#         print(f"No songs found in {folder}")

# Start video capture
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face, (64, 64)) / 255.0
        face = np.expand_dims(face, axis=-1)
        face = np.expand_dims(face, axis=0)

        preds = model.predict(face)
        emotion = emotion_labels[np.argmax(preds)]

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        #play_emotion_track(emotion)
        play_youtube_audio(emotion)
        break  # Only handle one face per frame

    cv2.imshow("Emotion Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
