# icnap hackathon
##  Time Series Classification and Regression using Transformers
## Contents
1. [Introduction](#introduction)
2. [Rocket transform](#Rocket-transform)
3. [Architecture](#Architecture)
4. [Installation](#Installation)
5. [Dataset](#making-dataset)
6. [Train the model](#train-the-model)
7. [Inspecting the model](#inspecting-the-model)


## Introduction
The codes are based on implementation of transformers for time series Classification with [Rocket transform](https://arxiv.org/abs/2012.08791) on Python 3, Keras, and TensorFlow to CLassify machine Data in Time series into categories such as in this case helmet, noise cancelling headphones, vest, eye safety goggles etc.

- It runs in Google colab [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/megh21/icnap-hack-22-Transformer) (GPU enabled environment) 

- This repo contains code for Time Series Classification and Regression using Transformers
- Time series classification - Task 1 - aux-code.ipynb
- LSTM Benchmark classification - Task 1 - LSTM_baseline.ipynb
- Time series regression - Task 1 - aux-code-bonus.ipynb
- Neural Network architecture
- Pretrained Transformer Model
- Pretrained LSTM Model
- Input Modelling architecture 

## Rocket transform
- RandOM Convolutional KErnal Transform) [Rocket could be implemented from](https://www.sktime.org/en/stable/api_reference/auto_generated/sktime.transformations.panel.rocket.MiniRocket.html)


## Architecture:
![image](https://user-images.githubusercontent.com/73994639/175145002-87d77094-fa80-45b6-8fc6-4f21182f6412.png)



## Installation
 1. Clone the repo `git clone (https://github.com/megh21/icnap-hack22-Transformer)`
 2. install dependencies
	  `cd icnap-hack22-Transformer`
	  `pip3 install -r requirements.txt` 


## Making Dataset

1. Find all Data into one single folder which are to be used for training
2. Data for Classification task is a binary classification based on FordA Dataset
3. Data for regression task is CNC Mill tool wear

## Train the model


To start training the network you can create your own config file or copy code from notebook to python script.
Instead of training a model from python script, we use the google Colab or upload notebook to Kaggle. 
    
## Inspecting the Model Loss 
![image](https://user-images.githubusercontent.com/73994639/175145072-164d0114-5a89-4829-90dd-500320121d8b.png)
![image](https://user-images.githubusercontent.com/73994639/175160898-e80e5330-2671-41d7-be35-adf2fd34758b.png)
## Inspecting the Model Training
![image](https://user-images.githubusercontent.com/73994639/175296122-26ef29b3-7476-4853-81a0-80e6201b05fe.png)

## LSTM Benchmark classification
![image](https://user-images.githubusercontent.com/73994639/175145123-7adc8646-8152-4340-a824-3a8220202ead.png)
## Transformer with Rocket classification
![image](https://user-images.githubusercontent.com/73994639/175160635-b4d835b1-26be-4de1-ab3f-aabbed7fe2ba.png)

