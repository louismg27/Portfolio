# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:04:50 2020

@author: claudia
"""


# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

#comenzando con el procesamiento de imagenes
from skimage import data

coins = data.coins()

print(coins.shape)
print(coins)

print(coins[1:10, 1:10])

import matplotlib.pyplot as plt

#Defino una funcion para mostrar una imagen por pantalla
# con el criterio que considro mas adecuado
def imshow(img):
    fig, ax= plt.subplots(figsize=(7,7))
    #El comando que realmente muestra la imagen
    ax.imshow(img,cmap=plt.cm.gray)
    #Para evitar que aparecan los numeros en los ejes
    ax.set_xticks([]), ax.set_yticks([])
    plt.show()
    
imshow(coins)

print(type(coins))

import numpy as np

print(np.max(coins))

a=np.arange(16).reshape((4,4))
print(a)
print(np.max(a))
print(np.max(a,axis=0))
print(np.max(a,axis=1))

max_per_column = np.max(coins,axis=0)
print(len(max_per_column))
print(max_per_column)

max_per_row = np.max(coins,axis = 1)
#vamos a representar ahora el maximo por filas
plt.plot(max_per_column)
plt.show()

umbral =160
binary_max_per_row= 255*(max_per_row>umbral)
plt.plot(binary_max_per_row)
plt.show()

test_coins = coins.copy()
test_coins[binary_max_per_row==0,:]=255
imshow(test_coins)

max_per_columns = np.max(coins,axis=0)
plt.plot(max_per_columns)
plt.show()

local_minima = np.array([75,130,180,240,290])

test_coins[:,local_minima]= 255
imshow(test_coins)