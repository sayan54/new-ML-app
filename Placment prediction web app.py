# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 20:34:15 2024

@author: User
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('model.sav', 'rb'))

# creating a function for Prediction

def placement_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
      return ' Placed'
    else:
      return 'Not Placed'
  
    
def main():
    
    
    # giving a title
    st.title('Campus Placement Prediction App')
    
    
    # getting the input data from the user
    
    
    Age = st.number_input('Enter Age',step=1.,format="%d")
    #Gender = st.selectbox("Your gender",("Male","Female"),index=None, placeholder="Select Gender...",)
    options = {"Male": 1, "Female": 2}
    selected_option = st.selectbox("Your gender", list(options.keys()), index=None, placeholder="Select Gender...")
    selected_value = options[selected_option]
    outst=st.write("You selected:", selected_value)
 
    Stream = st.number_input('Enter Stream',step=1.,format="%d")
    Internships = st.number_input('Enter number of Internships',step=1.,format="%d")
    CGPA = st.number_input('Enter CGPA',step=1.,format="%.2f")
    Hostel = st.number_input('Are you a Hosteler ?',step=1.,format="%d")
    HistoryOfBacklogs = st.number_input('Number of Backlogs',step=1.,format="%d")
    
    
    
    # code for Prediction
    detection = ''
    
    # creating a button for Prediction
    
    if st.button('Result'):
        detection = placement_prediction([Age, outst, Stream, Internships, CGPA, Hostel, HistoryOfBacklogs])
        
        
    st.success(detection)
    
    
    
    
    
if __name__ == '__main__':
    main()
  
