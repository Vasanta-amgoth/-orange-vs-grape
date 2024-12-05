#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import joblib
import numpy as np

# Load the pre-trained Random Forest model
model = joblib.load('citrus_pred.pkl')

# Function to predict the species
def predict_fruit(diameter, weight,red , green, blue):
    # Make the prediction using the model
    input_data = np.array([[diameter, weight,red , green, blue]])
    prediction = model.predict(input_data)
    

    species = ['orange','Grapefruit']
    return species[prediction[0]]

# Streamlit app
st.title("Orange vs Grapefruit predictor")
st.write("This is a simple app that predicts the fruit name  based on its features.")

# Input fields for user to provide data
diameter = st.number_input(' Fruit diameter', min_value=0.0, max_value=20.0, value=10.0)
weight = st.number_input('Fruit weight (cm)', min_value=0.0, max_value=300.0, value=150.0)
red = st.number_input('red (cm)', min_value=0.0, max_value=255.0, value=100.0)
green = st.number_input('green  (cm)', min_value=0.0, max_value=255.0, value=100.0)
blue = st.number_input('blue (cm)', min_value=0.0, max_value=255.0, value=100.0)
# Button to make prediction
if st.button('Predict Fruit'):
    Fruit_name = predict_fruit(diameter, weight,red , green, blue)
    st.write(f'The predicted fruit is: {Fruit_name}')


# In[ ]:




