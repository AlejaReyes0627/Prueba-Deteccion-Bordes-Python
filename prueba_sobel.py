import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from PIL import Image
from scipy.signal import convolve2d

img = Image.open('herramientas.jpg')
gray = np.mean(img, axis = 2)

Hx = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])) # Sorbel Filter
Hy = np.array(([-1, -2, -1], [0, 0, 0], [1, 2, 1])) # Prewitt filter
################Hx2 = np.array(([1, 2, 1], [0, 0, 0], [-1, -2, -1])) # DERICHE A VER SI SE PUEDE HACER
#Hx2 = np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0])) LAPLACIANO

#Hx2 = np.array(([2, -1, 2], [-1, -4, -1], [2, -1, 2])) otro laplaciano xD
#Hx2 = np.array(([-1, -1, -1], [-1, 8, -1], [-1, -1, -1])) otro laplaciano x3
Hx2 = np.array(([-1, -1, -1], [0, 0, 0], [1, 1, 1]))##roberto


SGx = convolve2d(gray, Hx)
SGy = convolve2d(gray, Hx)

PGx = convolve2d(gray, Hy)
PGy = convolve2d(gray, Hy)

Mgx = convolve2d(gray,Hx2)
Mgy = convolve2d(gray, Hx2)

Sobel_out = np.sqrt( np.square(SGx) + np.square(SGy) )
Prewitt_out = np.sqrt( np.square(PGx) + np.square(PGy) )
Laplaciano_out = np.sqrt( np.square(Mgx) + np.square(Mgy))

plt.title('Sobel')
plt.imshow(Sobel_out, cmap = 'gray')
plt.show()
plt.title('Prewitt')
plt.imshow(Prewitt_out, cmap = 'gray')
plt.show()
plt.title('Laplaciano')
plt.imshow(Laplaciano_out, cmap = 'gray')
plt.show()