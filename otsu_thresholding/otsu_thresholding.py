import cv2

from matplotlib import pyplot as plt

img=cv2.imread("gurultuluresim.JPG",0)

#Basit Thresholding:
#127'degerinden yuksek renk degerine sahip pikselleri 255 yapar.
_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#Otsu Thresholding
# Optimum esik degerini kendi hesaplar.
_,th2=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Orjinal resimdeki keskin gecisleri azaltmak icin 5x5 boyutunda
#kernel kullanarak 2 sigma degerinde blurlastirma uygulanir.
blur=cv2.GaussianBlur(img,(5,5),2)
#Blurlastirilmis goruntuye otsu thresholding uygulandiginda
#bozulmalarin daha da azaldigi gozlemlenebilir.
_,blur_otsu=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#resim verileri icin liste
imgs=[img,0,th1,
      img,0,th2,
      blur,0,blur_otsu]

#baslik stringleri icin liste
name_imgs=["Orjinal","Histogram","Basic_Threshold"
           ,"Orjinal","Histogram","Otsu_Threshold"
           ,"Blur","Histogram","Blur_Otsu"]

#9 verimiz var 3x3 boyutunda cizdirecegiz.
#bu yuzden 3 0..3 araliginda dongu
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(imgs[i*3])
    plt.title(name_imgs[i*3]),plt.xticks([]),plt.yticks([])
    #histogram cizdirme
    plt.subplot(3,3,i*3+2),plt.hist(imgs[i*3].ravel(),256)
    plt.title(name_imgs[i*3+1]),plt.xticks([]),plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(imgs[i*3+2],"gray")
    plt.title(name_imgs[i*3+2]),plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()