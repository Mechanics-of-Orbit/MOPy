import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Reading the image
img = mpimg.imread('UI_Functions\Resources\MOPy Cover_transparent.png')
#Printing the image array
imgplot = plt.imshow(img)
plt.show()