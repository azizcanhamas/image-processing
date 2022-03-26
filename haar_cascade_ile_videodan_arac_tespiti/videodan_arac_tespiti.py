import cv2

video=cv2.VideoCapture("video2.avi")
car_cascade=cv2.CascadeClassifier("cars.xml")

while True:
    ret,frame=video.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cars=car_cascade.detectMultiScale(gray_frame,1.01,8)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("frame",frame)
    if cv2.waitKey(100)&0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()