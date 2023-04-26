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
      with open("./data/AboutTheApp", "r") as file:
        message = file.read()

    st.sidebar.info(message)

    # get the input data from the user
    st.header('Input Features')
    # getting the input data from the user
    pregnancies = st.selectbox('Number of Pregnancies', range(11))
    glucose = st.selectbox('Glucose Level', range(40, 201, 10))
    blood_pressure = st.selectbox('Blood Pressure value', range(40, 141, 10))
    skin_thickness = st.selectbox('Skin Thickness value', range(5, 51, 5))
    insulin = st.selectbox('Insulin Level', range(0, 301, 20))
    bmi = st.selectbox('BMI value', range(100, 511, 5))
    diabetes_pedigree_function = st.selectbox('Diabetes Pedigree Function value', [round(x * 0.05, 2) for x in range(1, 101)])
    age = st.selectbox('Age of the Person', range(21, 81))
      
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
    
    
    
    
    
    
    
    
    
  
    
  
