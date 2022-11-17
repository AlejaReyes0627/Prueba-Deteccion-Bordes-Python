import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from PIL import Image
from scipy.signal import convolve2d

img = Image.open('herramientas.jpg')
gray = np.mean(img, axis = 2)

Hx = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])) # Sobel Filter
Hy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]]) #transpose even we could reduce it to np.transpose(Hx) but we done the simple way to get it.

SGx = convolve2d(gray, Hx)
SGy = convolve2d(gray, Hy)


Sobel_out = np.sqrt( np.square(SGx) + np.square(SGy) )

plt.title('Sobel')
plt.imshow(Sobel_out, cmap = 'gray')
plt.show()
