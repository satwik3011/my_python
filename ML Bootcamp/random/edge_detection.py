import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = gray.shape

        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)

        sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)

        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        canny = cv2.Canny(gray, 50, 100 )
        #cv2.imshow("My Window", frame)
        #cv2.imshow("Sobel X", sobel_x)
        #cv2.imshow("Sobel Y", sobel_y)
        #cv2.imshow("Sobel OR", sobel_OR)
        #cv2.imshow("Laplacian", laplacian)
        cv2.imshow("Canny", canny)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()