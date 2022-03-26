#Burada yuzleri "yuzverileri" klasorune kaydederek veri seti olusturacagiz.

import cv2
cam=cv2.VideoCapture(0)

detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#kisileri siniflandirmak icin degisken
i=0

#kisi id numarasi atama
kisi_id=input("ID bilgisi giriniz:")

while True:
    #kamera verisi okuma
    ret,frame=cam.read()
    #grayscale formata cevirme
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #bir framedeki yuzun alanini tespit etme
    faces=detector.detectMultiScale(gray_frame,scaleFactor=1.2,minNeighbors=5,minSize=(100,100),flags=cv2.CASCADE_SCALE_IMAGE)

    #tespit edilen yuzleri kaydetme
    for (x,y,w,h) in faces:
        #bir kisinin bir verisinin index numarasinin arttirilmasi
        i=i+1
        #yuzverileri klasoru altina face-kisi_id-index.jpg olarak yuz alaninin kaydediyoruz.
        cv2.imwrite("yuzverileri/face-"+kisi_id+"."+str(i)+".jpg",gray_frame[y:y+h,x:x+w])

        #verilerin benzersiz olmasi icin orneklem almayi yavaslatiyoruz. daha da arttirilabilir.
        cv2.waitKey(500)
    #20'den fazla yuz verisi olustuysa veri olusturmayi bitir. daha da arttirilabilir.
    if i>20:
        cam.release()
        cv2.destroyAllWindows()
        break