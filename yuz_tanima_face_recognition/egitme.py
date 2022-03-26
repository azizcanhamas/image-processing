import cv2
import os
import numpy as np

from PIL import Image

#cv2.LBPH yontemi ile training yapacagiz.
recognizer=cv2.face.LBPHFaceRecognizer_create()

#yuz tespiti icin haar cascade dosyasinin iceri aktarilmasi
cascadePath='haarcascade_frontalface_default.xml'
faceCascade=cv2.CascadeClassifier(cascadePath)

#veri setinin klasor adresi
path='yuzverileri'

def get_images_and_labels(path):
    #veri setini okuyoruz.
    image_paths=[os.path.join(path,f) for f in os.listdir(path)]
    images=[]
    labels=[]


    for image_path in image_paths:
        #L parametresi ile grayscale formatta bir veri okuyoruz.
        image_pil=Image.open(image_path).convert('L')

        #okudugumuz veriyi uint8 formatina ceviriyoruz.
        image=np.array(image_pil,'uint8')

        #dosya adindan kisi id numarasinin tespit edilmesi
        nbr=int(os.path.split(image_path)[1].split(".")[0].replace("face-",""))
        print(nbr)
        #verideki yuzlerin tespit edilmesi
        faces=faceCascade.detectMultiScale(image)

        #sirasi ile verideki yuzlerin ve veriye denk gelen labelin listelere eklenmesi
        for (x,y,w,h) in faces:
            images.append((image[y:y+h,x:x+w]))
            labels.append(nbr)
        return images,labels

images,labels=get_images_and_labels(path)

cv2.imshow("test",images[0])
cv2.waitKey(1)
#egitiim isleminin yuz verileri ve labellar ile baslatilmasi
recognizer.train(images,np.array(labels))
#egitilmis dosyanin kaydedilmesi
recognizer.write('training/trainer.yml')

cv2.destroyAllWindows()