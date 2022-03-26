#pip3 install pafy
#pip3 install youtube_dl --upgrade

#dislike_count hatasi verirse backend_youtube_dl.py dosyasinda
#53 ve 54. satirlar yorum satiri yapilmalidir.

import pafy
import cv2

#video linki
url="https://www.youtube.com/watch?v=F7mKD2Un65I"
vPaffy=pafy.new(url)
play=vPaffy.getbest(preftype="mp4")

kamera=cv2.VideoCapture(play.url)

while True:
    ret,frame=kamera.read()
    griton=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("griton",griton)
    cv2.imshow("frame", frame)

    if cv2.waitKey(30)&0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
