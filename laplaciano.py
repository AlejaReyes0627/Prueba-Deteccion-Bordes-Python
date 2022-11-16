
import cv2
import numpy as np
import matplotlib.pyplot as plt
 
 # Leer imagen
img = cv2.imread('lena-std.png')
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
 # Imagen de procesamiento en escala de grises
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
 # Algoritmo de Laplace
dst = cv2.Laplacian(grayImage, cv2.CV_16S, ksize=3)
Laplacian = cv2.convertScaleAbs(dst)
 
 # Se usa para mostrar etiquetas chinas normalmente
plt.rcParams['font.sans-serif'] = ['SimHei']
 
 # # Mostrar gráficos
 # títulos = [u'Imagen original ', u'Operador laplaciano']
# images = [lenna_img, Laplacian]
# for i in xrange(2):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()
 
 
 # Mostrar gráficos
plt.subplot (121), plt.imshow (img_RGB), plt.title ('imagen original'), plt.axis ('off') # el eje de coordenadas está desactivado
plt.subplot (122), plt.imshow (Laplacian, cmap = plt.cm.gray), plt.title ('Operador laplaciano'), plt.axis ('off')
plt.show()