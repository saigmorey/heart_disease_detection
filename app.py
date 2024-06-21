import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/saigo/OneDrive/Desktop/se_project/model.sav', 'rb'))


# creating a function for Prediction

def Heart_prediction(input_data):
    

    
    input_data_as_numpy=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    
    print(prediction)
    if (prediction[0]== 0):
      return'The person does not have Heart Disease '
    else:
      return 'The person is having Heart Disease '

  
def main():
    
    
    # giving a title
    st.title('Heart Disease Prediction')
    
    
    # getting the input data from the user
    
    age = st.number_input('Age (in years)  ')
        
    
    sex = st.number_input('Sex  1=Male;0=Female ')
        
    
    cp = st.number_input('Chest Pain types')
        
    
    trestbps = st.number_input('Resting Blood Pressure')
        
    
    chol = st.number_input('Serum Cholestoral in mg/dl')
        
    
    fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl')
        
    
    restecg = st.number_input('Resting Electrocardiographic results')
        
    
    thalach = st.number_input('Maximum Heart Rate achieved')
        
    
    exang = st.number_input('Exercise Induced Angina')
        
    
    oldpeak = st.number_input('ST depression induced by exercise')
        
    
    slope = st.number_input('Slope of the peak exercise ST segment')
        
    
    ca = st.number_input('Major vessels colored by flourosopy')
        
    
    thal = st.number_input('thal: 1= normal; 2 = fixed defect; 3 = reversable defect')
        
    
    
   
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        diagnosis = Heart_prediction([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    