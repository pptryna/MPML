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

# Judul web
st.title('Prediksi Feedback Konsumen')

# Input data dengan contoh angka valid untuk pengujian
Age = st.text_input('Age', '1')
Marital_Status = st.text_input('Marital Status', '0')
Occupation = st.text_input('Occupation', '1')
Educational_Qualifications = st.text_input('Educational Qualifications', '0')

feedback = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Convert input to appropriate data types
        Age = int(Age)
        Marital_Status = int(Marital_Status)
        Occupation = int(Occupation)
        Educational_Qualifications = int(Educational_Qualifications)
        
        # Melakukan prediksi
        feedback_prediction = feedback_model.predict([[Age,Marital_Status,Occupation,
                                                 Educational_Qualifications]])

        # Menentukan kategori feedback berdasarkan prediksi
        if feedback_prediction[0] == 'Positif':
            feedback = 'Positif'
        else:
            feedback = 'Negatif'
        
        st.success(feedback)

    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")