import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage import io
from skimage import color
from skimage import img_as_float
#mapeo en un intervalo de 0 a 255
imagen = data.astronaut()
#io.imshow(img)
#Mapeo en un interalo de 0 a 1
#img = img_as_float(img)

new_image = np.copy(imagen)
def artefactos_impulsivos(img,percentage):


# Ruido Blanco
num_outlier_black =  int(round((percentage/100.0)*img.size)) # np.ceil(amount * img.size * s_vs_p)
coordenadas = [np.random.randint(0, i - 1, size=num_outlier_black) for i in img.shape]
new_image[coordenadas] = 0

# Ruido  Negro
num_outlier_white = int(round((percentage/100.0)*img.size)) #np.ceil(amount* img.size * (1. - s_vs_p))
coordenadas = [np.random.randint(0, i - 1, size=num_outlier_white) for i in img.shape]
new_image[coordenadas] = 255

r= img[:,:,0]
r2= new_image[:,:,0]

fig, (ax1, ax2)= plt.subplots(ncols=2, figsize=(16,10), sharex=True, sharey=True)
ax1.imshow(r, cmap='gray')
ax2.imshow(r2, cmap='gray')
    plt.show()


def addOutlierToSignal(input_signal, percentage = 0.5):
    # input_signal: original dataset
    # percentage: percentage of samples that will be replaced by outliers
        
    # Adding num_outliers outiers to our dataset input_signal: num_outliers is given by the percentage of the samples
    # in the original dataset to be replaced by outliers
    num_outliers=int(round((percentage/100.0)*len(input_signal)))
    idx=np.round(np.random.uniform(0, len(input_signal)-1, size=num_outliers)).astype(int)
    
    # Max, min and sd of the dataset
    maxx=np.max(input_signal)
    minx=np.min(input_signal)
    sdx=np.std(input_signal)
    
    # Two halves for the outliers
    n1 = int(num_outliers/2)
    n2 = num_outliers - n1
    
    # Outlier samples to be included
    outliers=np.zeros(num_outliers)
    for i in range(0, num_outliers):
        if(i % 2 == 0):
            outliers[i]=np.random.uniform(minx-2*sdx, minx- sdx, size=1)
        else:
            outliers[i]=np.random.uniform(maxx + sdx, maxx + 2*sdx, size=1)
    
    # Initializing the noisy dataset
    noisy_signal=np.zeros(len(input_signal))
    
    # Original samples replaced by outliers
    cont=0
    for i in range(0, len(input_signal)):
        if(i in idx):
            noisy_signal[i]=outliers[cont]
            cont=cont+1
        else:
            noisy_signal[i]=input_signal[i]
    
    return noisy_signal


""" FUNCIONA
row,col,ch = img.shape
s_vs_p = 0.8
amount = 0.013
out = np.copy(img)
# Salt mode
num_salt = np.ceil(amount * img.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
out[coords] = 1

# Pepper mode
num_pepper = np.ceil(amount* img.size * (1. - s_vs_p))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in img.shape]
out[coords] = 0




r2= out[:,:,0]
ax2.imshow(r2, cmap='gray')
"""



"""

def sp_noise(image,prob):
'''
Add salt and pepper noise to image
prob: Probability of the noise
'''
       output = np.zeros(image.shape,np.uint8)
       thres = 1 - prob 
       for i in range(image.shape[0]):
           for j in range(image.shape[1]):
               rdn = random.random()
               if rdn < prob:
                   output[i][j] = 0
               elif rdn > thres:
                   output[i][j] = 255
               else:
                   output[i][j] = image[i][j]
       return output

image = cv2.imread('image.jpg',0) # Only for grayscale image
noise_img = sp_noise(image,0.05)
"""

"""

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray


"""


"""

prob=0.04
output = np.zeros(img.shape,np.uint8)
thres = 1 - prob
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        rdn = np.random.random()
        if rdn < prob:
            output[i][j] = 0
        elif rdn > thres:
            output[i][j] = 255
        else:
            output[i][j] = img[i][j]

noisy= img_as_float(output)
final= img + noisy
"""

