import cv2
import numpy as np
from PIL import Image
import pytesseract

#tesseract kurulmalidir. (Project Interpreter kismindan)

# pytesseract.pytesseract.tesseract_cmd=?????

kaynak_yolu=""
def metin_oku(img_yolu):
    img=cv2.imread(img_yolu)
    #resmimiz grayscale formatinda olmalidir.
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #okudugumuz resimde gurultuler olabilir
    kernel=np.ones((5,5),np.uint8)
    img=cv2.erode(img,kernel,iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    #renkli yazilarin etkilememesi icin
    img=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)

    cv2.imwrite("metin_okuma_islemli.jpg",img)

    #lang="tur" parametresi ile turkce karakter tanimasi saglanabilir.
    #ancak kurulumda belirtilmesi gerekiyor.
    sonuc=pytesseract.image_to_string(Image.open("metin_okuma_islemli.jpg"))

    return sonuc

print(metin_oku('a1.png'))