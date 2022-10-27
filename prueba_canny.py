import numpy as np
import cv2
 
# Cargamos la imagen
original = cv2.imread('lena-std.png')
# Convertimos a escala de grises
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
n = input("Put an odd number: ")
n2 = input("Put the min threeshold: ")
n1 = input("Put the max threeshold: ")
# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gris, (int(n),int(n)), 0)
# Detectamos los bordes con Canny
canny = cv2.Canny(gauss, int(n2), int(n1))
cv2.imshow("canny", canny) 
cv2.waitKey(0)