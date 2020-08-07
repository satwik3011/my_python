import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    ret, frame = cap.read()
    if ret:
        cv2.imshow("My Screen", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()