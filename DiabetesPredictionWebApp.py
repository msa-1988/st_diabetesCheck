# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 19:15:01 2021

@author: msali
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open("./data/trained_model.sav", 'rb'))


   
# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
 
def main():
    # set page title and favicon
    st.set_page_config(page_title='Diabetes Prediction Web App', page_icon=':pill:')

    # set page header
    st.title('Diabetes Prediction Web App')
    st.markdown('Please fill in the following details to predict if you have diabetes or not.')

    # create a sidebar
    st.sidebar.header('About')
    st.sidebar.info('This is a simple web app to predict if you have diabetes or not based on some common health indicators.')

    # get the input data from the user
    st.header('Input Features')
    Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1, value=0)
    Glucose = st.number_input('Glucose Level', min_value=0, max_value=300, step=1, value=0)
    BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1, value=0)
    SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1, value=0)
    Insulin = st.number_input('Insulin Level', min_value=0, max_value=1000, step=1, value=0)
    BMI = st.number_input('BMI', min_value=0, max_value=60, step=1, value=0)
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=5.0, step=0.1, value=0.0)
    Age = st.number_input('Age', min_value=1, max_value=120, step=1, value=1)

    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.write('')
    st.write('')
    
    # show the prediction result
    if diagnosis == '1':
        st.warning('Warning: You have a high chance of having diabetes. Please consult a doctor.')
    elif diagnosis == '0':
        st.success('Congratulations: You have a low chance of having diabetes.')
    else:
        st.info('Please fill in all the input fields and click on the "Diabetes Test Result" button to get the prediction result.')

if __name__ == '__main__':
    main()

   
    
    
    
    
    
    
    
    
    
    
  
    
  
