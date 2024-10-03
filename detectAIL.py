# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:48:09 2024

@author: ulp anyer
"""

import os
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from pdf2image import convert_from_path
import cv2


IMG_SIZE = (218, 218)
LR = 1e-3
MODEL_NAME = 'oldail_classification.h5'

model=load_model(MODEL_NAME)

# Function to extract images from PDF bytes
def extract_images_from_path(pdf_path):
    images = convert_from_path(pdf_path)[0]
    return images

# Function to preprocess and predict a single image
def predict_single_image(image_path, img_size):
    # Extract image from PDF
    image = extract_images_from_path(image_path)
    # Convert PIL image to numpy array
    numpy_image = pil_images_to_numpy(image)
    # Preprocess image
    preprocessed_image = preprocess_images(numpy_image, img_size)
    preprocessed_image = np.expand_dims(preprocessed_image, axis=-1)
    # Make prediction
    prediction = model.predict(preprocessed_image)
    return prediction

# Function to convert PIL images to numpy arrays
def pil_images_to_numpy(image):
    numpy_image = []
    numpy_image.append(np.array(image))
    return numpy_image

# Function to convert numpy arrays to grayscale and resize
def preprocess_images(images, size):
    processed_images = []
    for image in images:
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # Resize
        resized_image = cv2.resize(gray_image, size)
        processed_images.append(resized_image)
    return processed_images

def decode_label(one_hot_label):
    label_names = ['PK', 'BA', 'SIP', 'SLO', 'PDL',  'SPJBTL']
    index = np.argmax(one_hot_label)
    return label_names[index]

# Test a single image and print prediction


# image_path = '943-7.pdf'  # Path to the PDF file to be tested
# prediction = predict_single_image(image_path, IMG_SIZE)
# predlabel= decode_label(prediction)
# print("Prediction:", predlabel)


for x in range(1,1000):
    for y in range (1,11):
        currpath=f"{x}-{y}.pdf"
        if os.path.exists(currpath):
            prediction = predict_single_image(currpath, IMG_SIZE)
            predlabel= decode_label(prediction)
            new_name=f"{x}-{predlabel}.pdf"
            count=1
            while os.path.exists(new_name):
                new_name=f"{x}-{predlabel}_{count}.pdf"
                count+=1
            os.rename(currpath,new_name)
            print(f"{new_name} saved")
            