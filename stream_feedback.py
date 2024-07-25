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
def predict(Age,Marital_Status, Occupation,Educational_Qualifications):
    # Placeholder logic for prediction
    # You can replace this with actual model prediction logic
    if feedback_prediction == 'Positif':
            feedback = 'Positif'
    else:
            feedback = 'Negatif'
        

# Title of the application
st.title("UPI Payment Transactions Input")

# Form for user input
with st.form(key='feedback_form'):
 Age = st.text_input('Age', '1')
Marital_Status = st.text_input('Marital Status', '0')
Occupation = st.text_input('Occupation', '1')
Educational_Qualifications = st.text_input('Educational Qualifications', '0')

# Submit button for the form
submit_button = st.form_submit_button(label='Prediksi')

# Validation and prediction logic after form submission
if submit_button:
    if (is_valid_integer(Age) and is_valid_integer(Marital_Status) and is_valid_integer(Occupation) and is_valid_integer(Educational_Qualifications) ):
        
        st.success("All inputs are valid integers.")
        
        # Perform prediction
        prediction = predict(Age, Marital_Status, Occupation,Educational_Qualifications)
        
        # Display prediction result
        if prediction == 'Positive':
            st.success("feedback from customer: Positive")
        else:
            st.error("feedback from customer: negative")
    else:
        st.error("Please enter valid integer values.")