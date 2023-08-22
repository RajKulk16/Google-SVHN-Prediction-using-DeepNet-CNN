# SVHN Prediction using DeepNet CNN

Street View House Numbers (SVHN) is a real-world image dataset obtained from house numbers in Google Street View images.

## Key Achievements

- Implemented Custom CNN Model with Keras Tuner to tune hyperparameters.
- Achieved Model Accuracy: 81.15%

## Process Overview

1. **Data Conversion and Preprocessing:**
   - Converted `.mat` files to numpy format using scipy.
   - Preprocessed data by reducing channels and applying normalization.

2. **Custom CNN Model:**
   - Developed a Custom CNN model using Keras Tuner.
   - Total params: 15,698
   - Trainable params: 15,650
   - Non-trainable params: 48 (used for Batch Normalization)

3. **Dataset Link:**
   - [Download SVHN Dataset](http://ufldl.stanford.edu/housenumbers/)
