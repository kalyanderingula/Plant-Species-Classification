The Deep Learning for Plant Species Classification project aims to develop a highly accurate model for identifying different species of plants using deep learning techniques. With the increasing concern for environmental conservation and sustainable agriculture, it is essential to have accurate and efficient methods for plant species identification.
This project will utilize a dataset of plant images and employ convolutional neural networks (CNNs) for feature extraction and classification. Transfer learning techniques will be used to fine-tune pre-trained models to achieve high accuracy with limited training data. Various architectures such as ResNet, and VGG have been experimented with to find the best model for the task. This approach investigates the impact of different data augmentation techniques such as rotation, scaling, and cropping on the model's performance. The trained model has been tested on a separate validation dataset to evaluate its accuracy and efficiency.
The potential applications of the proposed work include developing plant identification, improving crop management, and aiding in plant conservation efforts. The primary outcome will contribute to the development of accurate and efficient methods for plant species classification and have significant implications for the fields of agriculture and ecology. 
Keywords: plant species classification, feature selection, feature extraction, CNN, deep learning.

Architecture for Plant Species Classification

The roles of the participating objects are as follows:

a)	Dataset

datasets were taken from Kaggle

b)	System 

Necessary pre-processing steps will be completed with the dataset before training with our algorithm.

c)	Training

Once after training the model will be saved for testing and classifying.

d)	Testing 

Once the CNN model is trained, evaluate its performance using the testing dataset that was set aside earlier

e)	Output/ Classification

User can upload the images of which to be classified and by using the saved model the images will be classified and predicted.

Module used

-NumPy

-IO

-OS

-Flask

-TensorFlow(keras)

-Matplotlib

-Pylab

-PIL.
