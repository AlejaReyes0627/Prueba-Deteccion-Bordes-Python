import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from PIL import Image
from scipy.signal import convolve2d

img = Image.open('herramientas.jpg')
gray = np.mean(img, axis = 2)

Hx = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1])) # Sobel Filter

SGx = convolve2d(gray, Hx)
SGy = convolve2d(gray, Hx)


Sobel_out = np.sqrt( np.square(SGx) + np.square(SGy) )

plt.title('Sobel')
plt.imshow(Sobel_out, cmap = 'gray')
plt.show()
