import numpy as np
import cv2

cap=cv2.VideoCapture('video.mp4')
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)
    cv2.imshow("fgmask",fgmask)
    cv2.imshow("orjinal",frame)
    if cv2.waitKey(30)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()