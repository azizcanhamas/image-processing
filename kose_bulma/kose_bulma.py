import cv2
import numpy as np


img=cv2.imread("kose_bulma.jpg")
#kose tespiti icin resmimiz grayscale ve float32 formatinda olmalidir.
griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
griton=np.float32(griton)

#gri resmimizde max 500 kose, 0.01 hassasiyetinde, 10px mesafelerle
#koseleri bulduruyoruz.
koseler=cv2.goodFeaturesToTrack(griton,500,0.01,10)
#kose konum piksel degerlerini float32'den int64'e cevirdik
koseler=np.int0(koseler)

#buldugumuz koseleri orjinal resimde isaretliyoruz.
for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Kamera ile Kenar Tespiti
# kamera=cv2.VideoCapture(0)
# while True:
#     ret,frame=kamera.read()
#     griton = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     griton = np.float32(griton)
#     koseler = cv2.goodFeaturesToTrack(griton, 500, 0.01, 10)
#     koseler = np.int0(koseler)
#
#     for kose in koseler:
#         x, y = kose.ravel()
#         cv2.circle(frame, (x, y), 3, 255, -1)
#
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(1)&0xFF==ord("q"):
#         break
# kamera.release()
# cv2.destroyAllWindows()