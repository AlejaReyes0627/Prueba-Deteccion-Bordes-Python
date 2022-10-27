import cv2

capture = cv2.VideoCapture(0)

while (capture.isOpened()):
    ret, frame = capture.read()
    if (ret == True):
        bordesCanny = cv2.Canny(frame, 100, 200)
        cv2.imshow("Canny", bordesCanny)
        if (cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
#hola