
"""
Created on Thu Oct  7 11:44:46 2021

@author: Danial Arab
"""
# Importing required libraries

from scipy.io import loadmat
import matplotlib.pyplot as plt
import cv2
import numpy as np
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Sequential 

# The dataset used in this project is Street View House Numbers (SVHN) Dataset -- format 2 (the cropped version), which
# can be downloaded from the link: http://ufldl.stanford.edu/housenumbers/

# STEP_1: Loading the datasets
training_dataset = loadmat('train_32x32.mat')
testing_dataset = loadmat('test_32x32.mat')

# STEP_2: Understanding the datasets: the training and testing datasets are 32*32*3 images in the form of .mat files 
# They are in dictionary data types, which need to be unwrapped. The corresponding labels are not required for this project.
# Because the datasets are in the form of a dictionary including a 4D matrix called X, including 32*32*3 images, they need to be extracted as follows:
images_training = training_dataset.get('X')
images_testing = testing_dataset.get('X')

# The data can also be saved through the following codes, just for having on a local machine, not required for this program. 
# =============================================================================
# for i in range(images_training.shape[3]):
#     cv2.imwrite('images_training/img_'+ str(i) +'.png', images_training[:,:,:,i])
#     i+=1
#     
# for i in range(images_testing.shape[3]):
#     cv2.imwrite('images_testing/img_'+ str(i) +'.png', images_testing[:,:,:,i])
#     i+=1
# 
# =============================================================================
# STEP_3: Conversion and reshaping: 
images_training = images_training.astype('float32') / 255.
images_testing = images_testing.astype('float32') / 255.

images_training = np.moveaxis(images_training, 3, 0)
images_testing = np.moveaxis(images_testing, 3, 0)

# STEP_4: Adding artifical noise to the datasets

mean = 0
var = 0.1
sigma = var**1
gaussian = np.random.normal(mean,sigma,size=images_training.shape)
gaussian = gaussian.reshape(images_training.shape)
images_training_noisy = images_training + gaussian

mean = 0
var = 0.1
sigma = var**1
gaussian = np.random.normal(mean,sigma,size=images_testing.shape)
gaussian = gaussian.reshape(images_testing.shape)
images_testing_noisy = images_testing + gaussian
    
# STEP_5: Clipping

images_training_noisy = np.clip(images_training_noisy, 0., 1.)
images_testing_noisy = np.clip(images_testing_noisy, 0., 1.)

# Displaying some noisy images
plt.figure(figsize=(20, 2))
for i in range(1,10):
    ax = plt.subplot(1, 10, i)
    plt.imshow(images_training[i,:,:,:].reshape(32, 32, 3), cmap="binary")
plt.show()

# STEP_6: Building the Model 
SIZE = 32
model = Sequential()
model.add(Conv2D(32, (3,3), activation = 'relu', padding = 'same', input_shape = (SIZE, SIZE, 3)))
model.add(MaxPooling2D((2,2), padding = 'same'))
model.add(Conv2D (8, (3,3), activation = 'relu', padding = 'same'))
model.add(MaxPooling2D((2,2), padding = 'same'))
model.add(Conv2D (8, (3,3), activation = 'relu', padding = 'same'))

model.add(MaxPooling2D ((2,2), padding = 'same'))

model.add(Conv2D (8, (3,3), activation = 'relu', padding = 'same'))
model.add(UpSampling2D((2,2)))
model.add(Conv2D (8, (3,3), activation = 'relu', padding = 'same'))
model.add(UpSampling2D((2,2))) 
model.add(Conv2D (32, (3,3), activation = 'relu', padding = 'same')) 
model.add(UpSampling2D((2,2)))
model.add(Conv2D (3, (3,3), activation = 'relu', padding = 'same'))

model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.summary()

model.fit(images_training_noisy, images_training, epochs=50, batch_size = 256, shuffle = True,
          validation_data = (images_testing_noisy, images_testing))

model.evaluate(images_testing_noisy, images_testing)

model.save('denoising_autoencoder.model')

denoised_img = model.predict(images_testing_noisy)

plt.figure(figsize=(40, 4))
for i in range(10):
    # the original image
    ax = plt.subplot(3, 20, i + 1)
    plt.imshow(images_testing_noisy[i].reshape(32, 32, 3), cmap="binary")
    
    # the denoised image
    ax = plt.subplot(3, 20, 40 +i+ 1)
    plt.imshow(denoised_img[i].reshape(32, 32, 3), cmap="binary")

plt.show()




