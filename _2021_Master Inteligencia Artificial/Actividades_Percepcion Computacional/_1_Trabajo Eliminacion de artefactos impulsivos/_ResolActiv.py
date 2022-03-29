import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage import io
from skimage import color
from skimage import img_as_float
from scipy import ndimage

from skimage import data,io,filters,feature,morphology
from skimage.morphology import square,disk
from scipy import ndimage as ndi

#mapeo en un intervalo de 0 a 255
imagen = data.astronaut()
#io.imshow(img)
#Mapeo en un interalo de 0 a 1
img = img_as_float(imagen)
percentage=0

def add_noisy(img,p):
    percentage=p/2
    new_image = np.copy(img)
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(16,10), sharex=True, sharey=True)

# Ruido Blanco
    num_outlier_black =  int(round((percentage/100.0)*img.size))  
    
    coordenadas = tuple([np.random.randint(0, i - 1, size=num_outlier_black) for i in img.shape])
    new_image[coordenadas] = 1
# Ruido  Negro
    num_outlier_white = int(round((percentage/100.0)*img.size)) 
    
    coordenadas = tuple([np.random.randint(0, i - 1, size=num_outlier_white) for i in img.shape])
    new_image[coordenadas] = 0

    r= img[:,:,0]
    r2= new_image[:,:,0]
    ax1.imshow(r, cmap='gray')
    ax2.imshow(r2, cmap='gray')
    
    return r2
   
img_noisy=add_noisy(img,10)


im_med = ndimage.median_filter(img_noisy, 3)
fig, ax1 = plt.subplots(ncols=1, figsize=(16,10), sharex=True, sharey=True)
ax1.imshow(im_med,cmap='gray')


imsobel= filters.sobel(im_med)
fig, ax1 = plt.subplots(ncols=1, figsize=(16,10), sharex=True, sharey=True)
ax1.imshow(imsobel,cmap='gray')
