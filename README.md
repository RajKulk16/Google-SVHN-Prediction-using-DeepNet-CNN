# Google SVHN Prediction using LeNet-5 and DeepNet CNN

Street View House Numbers (SVHN) is a real-world image dataset obtained from house numbers in Google Street View images.

## Key Achievement

- Implemented Custom (DeepNet) CNN Model with Keras Tuner and LeNet-5 architecture model for comparison.
- Achieved Model Accuracy:
  - CNN = 81.15% [SVHN - only CNN](https://github.com/RajKulk16/Google-SVHN-Prediction-using-DeepNet-CNN/blob/main/SVHN.ipynb)
  - LeNet-5 = 80.30% [LeNet-5 vs CNN](https://github.com/RajKulk16/Google-SVHN-Prediction-using-DeepNet-CNN/blob/main/Custom%20CNN%20vs%20LeNet-5.ipynb)

## Process Overview

1. **Data Conversion and Preprocessing:**
   - Converted `.mat` files to numpy format using scipy.
   - Preprocessed data by reducing channels and applying normalization.

2. **Custom CNN Model:**
   - Developed a Custom CNN model using Keras Tuner.
   - Total params: 15,698
   - Trainable params: 15,650
   - Non-trainable params: 48 (used for Batch Normalization)

3. **LeNet-5 Architecture:**
   - Implemented the traditional LeNet-5 alongside CNN to compare the base results of the both.

4. **Results:**
   - Although tuned-custom made CNN achieved higher results when compared to LeNet, LeNet showed stable increase and decrease in accuracy and loss respectively in comparison to CNN. 

5. **Dataset Link:**
   - [Download SVHN Dataset](http://ufldl.stanford.edu/housenumbers/)
