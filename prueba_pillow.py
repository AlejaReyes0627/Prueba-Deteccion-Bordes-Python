from importlib.resources import path
from PIL import Image, ImageFilter 
import cv2
  
image = Image.open("lena-std.png") 
  
image = image.convert() 

image = image.filter(ImageFilter.FIND_EDGES) 
image= image.filter(ImageFilter.SHARPEN)
image.save("edge.png") 