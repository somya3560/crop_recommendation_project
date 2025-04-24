import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌾 Crop Recommendation System")

# Input fields
N = st.slider("Nitrogen", 0, 140)
P = st.slider("Phosphorous", 5, 145)
K = st.slider("Potassium", 5, 205)
temperature = st.slider("Temperature (°C)", 8, 45)
humidity = st.slider("Humidity (%)", 10, 100)
ph = st.slider("pH", 3.5, 9.5)
rainfall = st.slider("Rainfall (mm)", 20, 300)

# Predict
if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"🌱 Recommended Crop: {prediction[0]}")
