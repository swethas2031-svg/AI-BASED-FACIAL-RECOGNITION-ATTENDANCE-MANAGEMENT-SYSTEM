import cv2
import face_recognition
import os
import pickle

path = "images"

images = []
names = []

for file in os.listdir(path):
    img = cv2.imread(os.path.join(path, file))
    if img is not None:
        images.append(img)
        names.append(os.path.splitext(file)[0])

encodings = []

for img in images:
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_encodings(rgb)
    if faces:
        encodings.append(faces[0])

with open("trainer/encodings.pkl", "wb") as f:
    pickle.dump((encodings, names), f)

print("Training completed successfully.")
