import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:
    ret,frame=kamera.read()
    cv2.imshow("frame", frame)

    #goruntude mavi renginin filtrelenmesi
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # cv2.imshow("hsv", hsv)
    alt_mavi=np.array([75,100,100])
    ust_mavi=np.array([130,255,255])
    mask=cv2.inRange(hsv,alt_mavi,ust_mavi)
    mavi=cv2.bitwise_and(frame,frame,mask=mask)
    # cv2.imshow("mavi", mavi)

    #EROSION-DILATION
    #5x5 boyutunda uint8 tipinde kernel tanimlanmasi
    kernel=np.ones((5,5),np.uint8)
    #erosion: gurultulyu siliyor.
    erosion=cv2.erode(mask,kernel,iterations=1)
    #dilation gurultuyu arttirir.
    dilation=cv2.dilate(mask,kernel,iterations=1)
    # cv2.imshow("erosion", erosion)
    # cv2.imshow("dilation", dilation)

    #OPENING-CLOSING
    #Closing : Filtreye uymayan renkleri filtrenin elemaniymis gibi gosterir.
    #Opening : Filtrenin elemani olan renkleri dahi gostermeyebilir.
    opening=cv2.morphologyEx(mavi,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mavi,cv2.MORPH_CLOSE,kernel)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)

    if cv2.waitKey(1)&0XFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()