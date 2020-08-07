import cv2
import dlib

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = dlib.get_frontal_face_detector()

while True:

    ret, frame = cap.read()

    if ret:
        faces = detector(frame)

        for face in faces:
            x = face.left()
            y = face.top()
            w = face.right() - x
            h = face.bottom() - y
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        cv2.imshow("My Window", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()