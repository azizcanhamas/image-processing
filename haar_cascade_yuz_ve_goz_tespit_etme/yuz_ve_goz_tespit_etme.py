import cv2


kamera=cv2.VideoCapture(0)

yuz_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
goz_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    ret,frame=kamera.read(0)

    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    yuzler=yuz_cascade.detectMultiScale(gray_frame,1.3,4)

    for (x,y,w,h) in yuzler:
        #framedeki yuzleri cizdiriyoruz.
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

        #tespit edilen yuzun bulundugu alanda goz arama islemi icin roi olusturuyoruz.
        roi_yuz_gray=gray_frame[y:y+h,x:x+w]

        #gozleri tespit ediyoruz.
        gozler = goz_cascade.detectMultiScale(roi_yuz_gray, 1.05, 9)

        #orjinal frame'e gozleri cizdiyoruz. (roi ile tespit yapildigi icin nokta kaydirma uygulandi)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(frame,(ex+x,ey+y),(ex+ew+x,ey+eh+y),(0,255,0),2)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()