
# Filtrado de convolución personalizado
import cv2
import numpy as np

 # Cargar imagen
image = cv2.imread('martillo.jpg',0)
image = cv2.resize(image,(800,800))
 # Kernel de convolución personalizado
 # Operador de borde Sobel
kernel_Sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
kernel_Sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]])
 # Detección de bordes canny k es el tamaño del núcleo gaussiano, t1, t2 son el tamaño del umbral
def Canny(image,k,t1,t2):
    img = cv2.GaussianBlur(image, (k, k), 0)
    canny = cv2.Canny(img, t1, t2)
    return canny
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

output_2 = cv2.filter2D(image, -1, kernel_Sobel_x)
output_4 = cv2.filter2D(image, -1, kernel_Laplacian_1)
output_5 = Canny(image,3,50,150)
#output_6 = kirsch(image)
 # Mostrar efecto de afilado
image = cv2.resize(image, (800, 600))
output_2 = cv2.resize(output_2, (800, 600))
output_4 = cv2.resize(output_4, (800, 600))
output_5 = cv2.resize(output_5, (800, 600))
#output_6 = cv2.resize(output_6, (800, 600))
cv2.imshow('Original Image', image)
cv2.imshow('sharpen_2 Image', output_2)
cv2.imshow('sharpen_4 Image', output_4)
cv2.imshow('sharpen_5 Image', output_5)
#cv2.imshow('sharpen_6 Image', output_6)
 # Pausa
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()