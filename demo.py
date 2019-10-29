from PIL import Image
import pytesseract

im = Image.open(r'C:\Users\SHUBH\Desktop\Python\menu.jpg')
print(im)
text = pytesseract.image_to_string(im)
print(text)
file = open('recognized.txt','w')
file.write(text)
file.close()
