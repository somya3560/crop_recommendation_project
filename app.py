# app.py
import streamlit as st
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("🌾 Crop Recommendation System")
st.markdown("Give temperature, humidity, and soil moisture to get the best crop recommendation.")

# Input fields
temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, step=0.1)
soil_moisture = st.number_input("🌱 Soil Moisture (%)", min_value=0.0, step=0.1)

# Prediction
if st.button("Recommend Crop"):
    input_data = np.array([[temperature, humidity, soil_moisture]])
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Recommended Crop: **{prediction}**")
