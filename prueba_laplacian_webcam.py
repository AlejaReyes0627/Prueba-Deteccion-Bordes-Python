import cv2

ddept=cv2.CV_16S
scale=1
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ref, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dst = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
    absx= cv2.convertScaleAbs(dst)
    cv2.imshow('edge', absx)
    if cv2.waitKey(1)==27:
        break
cv2.destroyAllWindows()
cap.release()