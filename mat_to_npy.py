import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os


mat = scipy.io.loadmat('C:/Users/rsk13/Desktop/Code/Projects/DL Projects/House Street/DO NOT UPLOAD/Cropped/train_32x32.mat')
Xtrain = mat['X']
ytrain = mat['y']

ytrain = np.where(ytrain==10,0,ytrain)

test_mat = scipy.io.loadmat('C:/Users/rsk13/Desktop/Code/Projects/DL Projects/House Street/DO NOT UPLOAD/Cropped/test_32x32.mat')
Xtest = test_mat['X']
ytest = test_mat['y']

ytest = np.where(ytest==10,0,ytest)

# Create the folder if it doesn't exist
if not os.path.exists('Numpy Files'):
    os.makedirs('Numpy Files')

# Save the arrays to numpy files in the "Numpy Files" folder
np.save('Numpy Files/Xtrain.npy', Xtrain)
np.save('Numpy Files/ytrain.npy', ytrain)
np.save('Numpy Files/Xtest.npy', Xtest)
np.save('Numpy Files/ytest.npy', ytest)
