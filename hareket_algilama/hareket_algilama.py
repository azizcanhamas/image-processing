import cv2
from datetime import datetime

#3 farkli zamanda cekilmis resmin farkini alarak
#hareket olup olmadigini anlayacagiz.
def fark_image(t0,t1,t2):
    #mutlak cikarma islemleri
    fark1=cv2.absdiff(t2,t1)
    fark2=cv2.absdiff(t1,t0)
    #sonuclara and islemi uyguluyoruz.
    return cv2.bitwise_and(fark1,fark2)

#HASSASIYET AYARI
# 640*480*3 = 921600 (frame_en * frame_boy * kanal_sayisi)
esik_deger=50000

#dahili kameradan veri okunacak.
kamera=cv2.VideoCapture(0)

t_eksi=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)

# saniye cinsinden orneklem zamani icin baslangic degeri tutuyoruz.
zamanKontrol = datetime.now().strftime("%Ss")
while True:
    #ekrana frame yansitiyoruz.
    cv2.imshow("pencere", kamera.read()[1])

    #eger 3 resim arasindaki fark 50000 degerinden fazlaysa hareket olmustur ve orneklem zamani dolduysa
    if cv2.countNonZero(fark_image(t_eksi,t,t_arti))>esik_deger and zamanKontrol!=datetime.now().strftime("%Ss"):
        #hareket resmini oku
        fark_resim=kamera.read()[1]
        #tarih bilgisiyle jpg formatinda kaydet
        cv2.imwrite(datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss%f")+'.jpg',fark_resim)
        #orneklem zamanini guncelle
        zamanKontrol=datetime.now().strftime('%Ss')
        #fotograflari guncelle.
        t_eksi=t
        t=t_arti
        t_arti=cv2.cvtColor(kamera.read()[1],cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()