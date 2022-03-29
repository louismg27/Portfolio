# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 09:25:28 2020

@author: claudia
"""
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage import io
from skimage import color
from skimage import img_as_float
#mapeo en un intervalo de 0 a 255
img = data.astronaut()
io.imshow(img)
#Mapeo en un interalo de 0 a 1
img = img_as_float(img)

r= img[:,:,0]
g= img[:,:,1]
b= img[:,:,2]

fig, (ax1, ax2, ax3)= plt.subplots(ncols=3, figsize=(16,10), sharex=True, sharey=True)
ax1.imshow(r, cmap='gray')
ax2.imshow(g, cmap='gray')
ax3.imshow(b, cmap='gray')


red_image= np.zeros((512,512,3))
red_image[:,:,0] = np.zeros((512,512))
red_image[:,:,1] = b
red_image[:,:,2] = np.zeros((512,512))

green_image = np.zeros((512,512,3))
green_image[:,:,0]= np.zeros((512,512))
green_image[:,:,1]= g
green_image[:,:,2]= np.zeros((512,512))

blue_image = np.zeros((512,512,3))
blue_image[:,:,0]= np.zeros((512,512))
blue_image[:,:,1]= np.zeros((512,512))
blue_image[:,:,2]= b

fig, (ax1, ax2, ax3)= plt.subplots(ncols=3, figsize=(16,10), sharex=True, sharey=True)
ax1.imshow(red_image)
ax2.imshow(green_image)
ax3.imshow(blue_image)


purple_image= np.zeros((512,512,3))
purple_image[:,:,0] = r
purple_image[:,:,2] = b

yellow_image = np.zeros((512,512,3))
yellow_image[:,:,0]= r
yellow_image[:,:,1]= g

mixed_image = np.zeros((512,512,3))
mixed_image[:,:,0]= r
mixed_image[:,:,1]= g
mixed_image[:,:,2]= b

fig, (ax1, ax2, ax3)= plt.subplots(ncols=3, figsize=(16,10), sharex=True, sharey=True)
ax1.imshow(purple_image)
ax2.imshow(yellow_image)
ax3.imshow(mixed_image)