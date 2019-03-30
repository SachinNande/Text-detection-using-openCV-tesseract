import cv2
import numpy as np
import pytesseract
from PIL import Image


src_path = "/home/sachin/Desktop/PROJECT/code/det.py"

def get_string(img_path):
    
    img = cv2.imread('image.png')

    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    kernel = np.ones((1, 1), np.uint8)
    img1 = cv2.dilate(img, kernel, iterations=1)
    img2 = cv2.erode(img, kernel, iterations=1)
    cv2.imshow('Erosion', img1) 
    cv2.imshow('Dilation', img2) 
    cv2.waitKey(0)
    
     

    
    cv2.imwrite(src_path + "removed_noise.png", img)

    
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    
    cv2.imwrite(src_path + "thres.png", img)

    
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    
    

    return result



print ('Recognised Text is as Follows\r\n')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print get_string(src_path + " ")


print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print (" Done ")
