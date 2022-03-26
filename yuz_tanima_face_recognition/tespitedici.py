# "training" adinda klasor olusturulur
# "yuzverileri" adinda klasor olusturulur
# "haarcascade_frontalface_default.xml" dosyasi import edilir.
#  3 adet python dosyasi olusturulacak
#       veriSetiOlusturucu.py , egitme , tespitedici

#Yuz tanima icin cesitli yontemler vardir.
#Ornegimizde Local Binary Patterns Histogram yontemi kullanilacak.(LBPH)

import cv2

#LBPH dosyasinin ve frontalface haar dosyasinin okunmasi
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("training/trainer.yml")
cascadePath="haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(cascadePath)

#gercek zamanli test icin dahili kameraya baglaniyoruz.
cam=cv2.VideoCapture(0)
while True:
    #bir frame okuyoruz.
    ret,frame=cam.read()
    #okudugumuz frame'i grayscale formata ceviriyoruz.
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #resimdeki yuzleri tespit ediyoruz.
    faces=faceCascade.detectMultiScale(gray_frame,scaleFactor=1.2,minNeighbors=5)
    for (x,y,w,h) in faces:
        #tespit ettigimiz ilk yuzu taniyip tanimadigimiza bakiyoruz.
        tahmin_edilen_kisi,conf=recognizer.predict(gray_frame[y:y+h,x:x+w])
        print(tahmin_edilen_kisi)
        cv2.rectangle(frame,(x-10,y-10),(x+w+10,y+h+10),(225,0,0),2)
        #eger predict metodundan 1 donduyse bu kisi Aziz'dir.
        if (tahmin_edilen_kisi==1):
            tahmin_edilen_kisi="Aziz Can"
        elif (tahmin_edilen_kisi==2):
            tahmin_edilen_kisi="Aziz Sancar"
        else:
            tahmin_edilen_kisi = "Bilinmeyen Kisi"

        #Orjinal goruntude siniflandirma icin yazi yazdiriyoruz.
        fontFace=cv2.FONT_HERSHEY_SIMPLEX
        fontScale=1
        fontColor=(255,255,0)
        cv2.putText(frame,str(tahmin_edilen_kisi),(x,y+h),fontFace,fontScale,fontColor)
        cv2.imshow("resim",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()