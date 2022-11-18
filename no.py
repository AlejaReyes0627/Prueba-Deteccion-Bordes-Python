
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from PIL import Image
from scipy.signal import convolve2d

#Metodo Sobel

 # Cargar imagen
img = Image.open('martillo.jpg')
gray = np.mean(img, axis = 2)

Hx = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])) # Sobel Filter
Hy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]) #transpose even we could reduce it to np.transpose(Hx) but we done the simple way to get it.

SGx = convolve2d(gray, Hx)
SGy = convolve2d(gray, Hy)

Sobel_out = np.sqrt( np.square(SGx) + np.square(SGy) )

plt.title('Sobel')
plt.imshow(Sobel_out, cmap = 'gray')
plt.show()


#Metodo Laplaciano

 # Cargar imagen
image = cv2.imread('martillo.jpg',0)
image = cv2.resize(image,(800,800))

 # Kernel de convolución de Laplace
kernel_Laplacian_1 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]])
kernel_Laplacian_2 = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]])
 # Los siguientes dos núcleos de convolución no tienen invariancia de rotación
kernel_Laplacian_3 = np.array([
    [2, -1, 2],
    [-1, -4, -1],
    [2, 1, 2]])
kernel_Laplacian_4 = np.array([
    [-1, 2, -1],
    [2, -4, 2],
    [-1, 2, -1]])

output_4 = cv2.filter2D(image, -1, kernel_Laplacian_1)
 # Mostrar efecto de afilado
image = cv2.resize(image, (800, 600))
output_4 = cv2.resize(output_4, (800, 600))
cv2.imshow('laplacian', output_4)
 # Pausa
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
    
    
