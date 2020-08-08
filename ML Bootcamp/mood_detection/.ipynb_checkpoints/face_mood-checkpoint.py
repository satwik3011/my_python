import cv2
import numpy as np
import dlib
from sklearn.neighbors import KNeighborsClassifier

data = np.load("mood_data.npy")

X = data[:, 1:].astype(int)
y = data[:, 0]

model = KNeighborsClassifier()
model.fit(X, y)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../datasets/shape_predictor_68_face_landmarks.dat")

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:

        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y

        landmarks = predictor(gray, face)
        expression = np.array([[point.x - face.left(), point.y - face.top()] for point in landmarks.parts()[17:]])

        out = model.predict([expression.flatten()])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, str(out[0]), (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

    if ret:
        cv2.imshow("My Screen", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()