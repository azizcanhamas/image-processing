#YONTEM:
# Hareketli videolarda arka plan temizleme uygulanacaktir. Bu sayede
# arka plan komple siyah olacak ve hareket eden arac komple beyaz olacaktir.
# Bu islemde tespit edilen aracin bir agirlik merkezi olusacaktir.
# Araclar iki seritte ilerlemektedir. Biz sag seritte bir alan ve sol seritte
# bir alan belirleyecegiz. Aracin agirlik merkezi belirledigimiz alan icerisinde
# ise arac sayisini bir arttiracagiz.

import cv2
import numpy as np

fgbg=cv2.createBackgroundSubtractorMOG2()

video=cv2.VideoCapture("video.avi")

#Arac sayisini tutacagiz.
i=0

#tespit icin minimum alan esik degeri
#bu deger moments['m00'] degerine gore secilmistir.
minArea=2600

while True:
    ret,frame=video.read()

    #Video bitince hata verme sorunu icin
    if ret==False:
        break
    #0.02 hassasiyet
    fgmask=fgbg.apply(frame,None,0.02)

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(fgmask,kernel,iterations=5)
    dilation=cv2.dilate(erosion,kernel,iterations=2)

    moments=cv2.moments(dilation,binaryImage=True)

    #SOL_SERIT_CIZGILERI

    # (aracin agirlik merkezi belirlenen karenin icine denk gelirse arac sayisini bir arttir)
    #dikey_cizgiler
    cv2.line(frame, (24, 1), (25, 175), (255, 255, 0), 2)
    cv2.line(frame, (51, 1), (51, 175), (255, 255, 0), 2)
    #yatay cizgileri
    cv2.line(frame, (2, 33), (317, 42), (255, 255, 0), 2)
    cv2.line(frame,(2,63),(320,53),(255,255,0),2)

    #SAG_SERIT_CIZGILERI
    # dikey_cizgiler
    cv2.line(frame, (24, 1), (25, 175), (255, 255, 0), 2)
    cv2.line(frame, (51, 1), (51, 175), (255, 255, 0), 2)
    # yatay cizgileri
    cv2.line(frame, (2, 120), (317, 70), (255, 255, 0), 2)
    cv2.line(frame, (2, 151), (320, 80), (255, 255, 0), 2)

    #m00 degeri 2600 degerinden buyukse bir arac gecmistir.
    if moments['m00']>=minArea:
        #agirlik merkezinin x koordinat degeri
        x=int(moments['m10']/moments['m00'])
        # agirlik merkezinin y koordinat degeri
        y = int(moments['m01'] / moments['m00'])

        # print("x:",#agirlik merkezinin x koordinat degeri
        #         x=int(moments['m10']/moments['m00'])x,"    y:",y)

        #belirledigimiz alanlar icindeyse arac sayisini bir arttir
        #arac cok uzunsa sapma yaratabilir.
        if x>40 and x<55 and y>45 and y<150:
            i+=1
    text="count:"+str(i)
    cv2.putText(frame,text,(245,15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
    # cv2.imshow("erosion-dilation",dilation)
    # cv2.imshow("masked",fgmask)
    cv2.imshow("frame",frame)
    if cv2.waitKey(30)&0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()