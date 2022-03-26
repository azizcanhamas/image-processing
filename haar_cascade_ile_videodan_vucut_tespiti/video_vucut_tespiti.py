import cv2

video=cv2.VideoCapture("video.mp4")

body_cascade=cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    ret,frame=video.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    bodys=body_cascade.detectMultiScale(gray_frame,1.1,4)

    for (x,y,w,h) in bodys:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",frame)
    if cv2.waitKey(60)&0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()