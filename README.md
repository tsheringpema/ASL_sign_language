# ASL_sign_language
![page](https://github.com/user-attachments/assets/34272057-cb28-4cf9-8bcd-ae27c1eb17de)

## Sign Language Letter Classification 
### Overview 
This project is a web application that uses a custom-trained Convolutional Neural Network (CNN) to classify American Sign Language (ASL) letters from hand gesture images. Built with Django and TensorFlow, it allows users to upload an image and get the predicted letter.
### About Datasets 
This project uses the American Sign Language (ASL) Alphabet dataset available on [Kaggle](https://www.kaggle.com/datasets/lexset/synthetic-asl-alphabet/data).
Each image represents a hand gesture corresponding to an English alphabet letter. The dataset contains 27,000 labeled images spread across 27 folders (one per class) plus 1 folder which contain random backgrounds.

For this project, only 25 classes were used:
- The 24 static letters (A–Y, excluding 'J' and 'Z')
- One 'Blank' class for neutral/no gesture

### Preview 
![preview](https://github.com/user-attachments/assets/92b98a47-1a95-4e09-8859-0d71232cade8)

Using the above shown app interface, we can upload an image of a hand gesture and predict the ASL (American Sign Language) letters. It will only support letters A to Y excluding J as shown above in the preview. 

