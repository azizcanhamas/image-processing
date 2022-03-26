import cv2

kamera=cv2.VideoCapture(0)
yuz_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,frame=kamera.read()
    gri_ton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_cascade.detectMultiScale(gri_ton,1.1,4)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
