import re
import os
import csv
import cv2
import numpy as np
import pandas as pd
import pytesseract
from PIL import Image
from pytesseract import image_to_string

path ="C:\\Users\\dilip.rb197\\Desktop\\Pyhton Image processing\\img\\test_case\\"
image = "set5.jpg"   # image name 

src_path = path+image

pytesseract.pytesseract.tesseract_cmd = "C:/Users/dilip.rb197/AppData/Local/Tesseract-OCR/tesseract"
TESSDATA_PREFIX = "C:/Users/dilip.rb197/AppData/Local/Tesseract-OCR"


import cv2
import numpy as np

# reading the image
#img = cv2.imread(src_path)

# Rescale the image, if needed.
#img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC) #use

#----------------- referance case of size -----------------
img = cv2.imread(src_path,cv2.IMREAD_COLOR)
W=1000
height, width, depth = img.shape
imgScale = W/width
newX,newY = img.shape[1]*imgScale, img.shape[0]*imgScale
img = cv2.resize(img, None, fx=int(newX), fy=int(newY), interpolation=cv2.INTER_CUBIC) #use
#------------------------------------------------------

rgb_planes = cv2.split(img)

result_planes = []
result_norm_planes = []
for plane in rgb_planes:
    dilated_img = cv2.dilate(plane, np.ones((7,7), np.uint16))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(plane, bg_img)
    norm_img = diff_img.copy() # Needed for 3.x compatibility
    _, thr_img = cv2.threshold(norm_img, 230, 0, cv2.THRESH_TRUNC)
    fi_img = cv2.normalize(diff_img, thr_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    result_planes.append(diff_img)
    result_norm_planes.append(fi_img)

result = cv2.merge(result_planes)
result_norm = cv2.merge(result_norm_planes)

cv2.imwrite(path+'shadows_out.png', result)   
cv2.imwrite(path+'shadows_out_norm.png', result_norm)  
text = image.replace('.jpg','.txt')
if text in os.listdir(path):
    print('file is present so removing')
    os.remove(path+text)
    
else :
    pass



file = open(path+text,'w',encoding='utf-8')
def get_string():
    print("reading the text from the image and grouping it ...........")
    result = pytesseract.image_to_string(Image.open(path+'shadows_out_norm.png').convert("RGB"), lang='eng+ara')
    print(result)
    file.write(result)
    file.close()

print('--- Start recognize text from image ---')
get_string()


def mysplit(s):
##     head = s.rstrip('0123456789.0\n')
     head = s.rstrip('0123456789.0ABCD~( \n')
     tail = s[len(head):]
     #data_wrt.write((lst))
     f_data = head,tail
     #print(f_data)
##     print(type(f_data))
#		with open('C:\\Users\\dilip.rb197\\Desktop\\Pyhton Image processing\\img\\test_case\\Sharton_Grillchicken_sample.txt','a',encoding='utf-8')  as f:
 #        writer=csv.writer(f, delimiter="|", lineterminator="\r")
 #        writer.writerows([f_data])
     
     return head, tail

row = open(path+text,'r',encoding='utf-8')
for i in row.readlines():
    #print(type(i))
    lst=str([mysplit(s) for s in [i]])
    #print(lst)
print("------ Done -------")
