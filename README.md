# Garbage-Classifier
AI enabled garbage classifier

## Objective:
To create a model that automates the process of segregating waste, creating a high-tech garbage sorting system. We have used diverse dataset of images representing different types of garbage items. The proposed model distinguishes between the garbage types based on features such as shapes, textures, and patterns within the images.


## Dataset EDA
*	Total images : 2527
*	Image dimensions : 512 X 384
*	Format : JPEG
*	No.of Image class : 6(metal, glass, paper, trash, cardboard,plastic)
  ![Screenshot 2024-12-19 231834](https://github.com/user-attachments/assets/2671ae4e-780d-46d7-aa27-908c681d8543)


## Data Preprocessing:
* As the class distribution is unbalanced, we have carried out image augmentation on the different classes to make them have the same number of images. 

* It includes making minor changes to the dataset to generate new data points.  In the case of image augmentation, we make geometric and color space transformations (flipping, resizing, cropping, brightness, contrast) to increase the size and diversity of the training set. 

* Post augmentation all classes have 600 images each.
![Screenshot 2025-01-09 103931](https://github.com/user-attachments/assets/eeeb5670-ac89-4e8d-a94b-649d1c0f168e)


## Model Selection:
After extensive testing on various models such as basic CNN and various flavours of Resnet models, we have chosen the pretrained Resnet 50 V2 model.ResNet50V2 incorporates some improvements and optimizations over the original ResNet architecture.
Added custom layers (global average pooling, dense layers, dropout) to adapt to the garbage classification task.

![Screenshot 2025-01-09 104119](https://github.com/user-attachments/assets/2b4af4da-a37b-41fc-b477-2940c20291ff)


## Model Evaluation:
Model exhibits a testing accuracy of 92.5 %
We have also tested the model on images captured by us: pictures various garbage items found in our own homes. Model displayed very good accuracy on these images too.

![Screenshot 2025-01-09 104119](https://github.com/user-attachments/assets/b6995c39-f746-4e87-83fb-e9ab60a2bbea)

## Challenges in implementation
The similarity between categories: for example, glass and plastic objects—can make them appear similar in photos, which presents another difficulty for model trying to tell them apart.
