import pickle
import streamlit as st

# Membaca model
try:
    with open('feedback_model.sav', 'rb') as file:
        feedback_model = pickle.load(file)
except FileNotFoundError:
    st.error("File model tidak ditemukan. Pastikan file berada di jalur yang benar.")
except Exception as e:
    st.error(f"Error saat memuat model: {e}")

# Function to validate if the input is an integer
def is_valid_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to simulate prediction logic
def predict(Age, Gender, Marital_Status, Occupation, Monthly_Income, Educational_Qualifications, Family_size):
    # Placeholder logic for prediction
    # You can replace this with actual model prediction logic
    input_data = [[int(Age), int(Gender), int(Marital_Status), int(Occupation), int(Monthly_Income), int(Educational_Qualifications), int(Family_size)]]
    feedback_prediction = feedback_model.predict(input_data)
    
    # Menentukan kategori feedback berdasarkan prediksi
    if feedback_prediction[0] == 1:
        feedback = 'Positif'
    else:
        feedback = 'Negatif'
    
    return feedback

# Title of the application
st.title("Prediksi Feedback Customer")

# Form for user input
with st.form(key='feedback_form'):
    Age = st.text_input('Age', '1')
    Gender = st.text_input('Gender', '0')
    Marital_Status = st.text_input('Marital Status', '0')
    Occupation = st.text_input('Occupation', '1')
    Monthly_Income = st.text_input('Monthly Income', '0')
    Educational_Qualifications = st.text_input('Educational Qualifications', '0')
    Family_size = st.text_input('Family Size', '1')
    
    # Submit button for the form
    submit_button = st.form_submit_button(label='Prediksi')

# Validation and prediction logic after form submission
if submit_button:
    if (is_valid_integer(Age) and is_valid_integer(Gender) and is_valid_integer(Marital_Status) and is_valid_integer(Occupation) and is_valid_integer(Monthly_Income) and is_valid_integer(Educational_Qualifications) and is_valid_integer(Family_size)):
        st.success("All inputs are valid integers.")
        
        # Perform prediction
        prediction = predict(Age, Gender, Marital_Status, Occupation, Monthly_Income, Educational_Qualifications, Family_size)
        
        # Display prediction result
        if prediction == 'Positif':
            st.success("Feedback from customer: Positif")
        else:
            st.error("Feedback from customer: Negatif")
    else:
        st.error("Please enter valid integer values.")
