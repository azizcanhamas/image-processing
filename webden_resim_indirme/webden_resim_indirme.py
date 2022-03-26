import cv2
#webden resim cekmek icin
from skimage import io

adresler=["https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png","https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png"]

for adres in adresler:
    print("%s yukleniyor."%(adres))
    resim=io.imread(adres)
    resim=cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)
    cv2.imshow("resim",resim)
    print("Yukleme tamamlandi.")
    cv2.waitKey(0) #Her resim yuklendiginde q basilmalidir.