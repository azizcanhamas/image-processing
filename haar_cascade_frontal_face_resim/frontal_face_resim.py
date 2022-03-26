import cv2

img=cv2.imread("kalabalik2.jpg")

#haar_cascade algoritmasinin dosya uzerinden iceri alinmasi
yuz_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#haar cascade icin orjinal fotograf grayscale yapilmalidir.
gri_ton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#grayscale fotograf uzerinde %10 buyuterek 2 kez teyit ettirerek detect
#geri donus degeri olarak her yuz icin x,y,w,h degeri doner
yuzler=yuz_cascade.detectMultiScale(gri_ton,1.1,2)

#orjinal fotograf uzerine yuzleri cizdiyoruz.
for (x,y,w,h) in yuzler:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("yuzler",img)
cv2.waitKey(0)
cv2.destroyAllWindows()


