# Garbage-Classifier
AI enabled garbage classifier

## Objective:
To create a model that automates the process of segregating waste, creating a high-tech garbage sorting system. We have used diverse dataset of images representing different types of garbage items. The proposed model distinguishes between the garbage types based on features such as shapes, textures, and patterns within the images.


## Dataset EDA
*	Total images : 2527
*	Image dimensions : 512 X 384
*	Format : JPEG
*	No.of Image class : 6


## Data Preprocessing:
As the class distribution is unbalanced, we have carried out image augmentation on the different classes to make them have the same number of images.
Post augmentation all classes have 600 images each


## Model Selection:
After extensive testing on various models such as basic CNN and various flavours of Resnet models, we have chosen the pretrained Resnet 50 V2 model.ResNet50V2 incorporates some improvements and optimizations over the original ResNet architecture.
Added custom layers (global average pooling, dense layers, dropout) to adapt to the garbage classification task.

## Model Evaluation:
Model exhibits a testing accuracy of 92.5 %
We have also tested the model on images captured by us: pictures various garbage items found in our own homes. Model displayed very good accuracy on these images too.

## Challenges in implementation
The similarity between categories: for example, glass and plastic objects—can make them appear similar in photos, which presents another difficulty for model trying to tell them apart.
