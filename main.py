from skimage import io
import matplotlib.pyplot as plt

im1 = io.imread('test_data.tiff')
y = []
for i in range(im1.shape[0]):
    y.append(im1[i,:,:].mean())

x = [*range(0, im1.shape[0], 1)]
plt.plot(x,y)
plt.show()