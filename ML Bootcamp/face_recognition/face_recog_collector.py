import cv2
import numpy as np
import os
import dlib

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = dlib.get_frontal_face_detector()

name = input("Enter your name: ")

frames = []
outputs = []

while True:

    ret, frame = cap.read()
    gray = []

    if ret:

        faces = detector(frame)

        for face in faces:
            x = face.left()
            y = face.top()
            w = face.right() - x
            h = face.bottom() - y

            cut = frame[y:y+h, x:x+w]
            fix = cv2.resize(cut, (100, 100))
            gray = cv2.cvtColor(fix, cv2.COLOR_BGR2GRAY)
            cv2.imshow("My Face", gray)

        cv2.imshow("My Screen", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("c"):
        frames.append(np.array(gray).flatten())
        outputs.append([name])

X = np.array(frames)
y = np.array(outputs)

data = np.hstack([y, X])

f_name = "face_data.npy"

if os.path.exists(f_name):
    old = np.load(f_name)
    data = np.vstack([old, data])

np.save(f_name, data)

cap.release()
cv2.destroyAllWindows()