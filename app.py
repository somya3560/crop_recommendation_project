import streamlit as st
import numpy as np
import tensorflow as tf

# Load the trained Keras model
model = tf.keras.models.load_model("model/crop_model.h5")

# Streamlit app UI
st.set_page_config(page_title="Crop Recommendation App", layout="centered")
st.title("🌾 Crop Recommendation System")
st.write("Enter the environmental values below:")

# Input fields
temperature = st.number_input("🌡️ Temperature (°C)", min_value=0.0, max_value=100.0, step=0.1)
humidity = st.number_input("💧 Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
soil_moisture = st.number_input("🌱 Soil Moisture (%)", min_value=0.0, max_value=100.0, step=0.1)

# Predict button
if st.button("Predict Best Crop"):
    # Prepare input
    input_data = np.array([[temperature, humidity, soil_moisture]])
    
    # Predict crop index
    prediction = model.predict(input_data)
    crop_index = np.argmax(prediction)
    
    # Define crop labels (update if your model uses different ones)
    crops = [
        'apple', 'banana', 'blackgram', 'chickpea', 'coconut', 'coffee',
        'cotton', 'grapes', 'jute', 'kidneybeans', 'lentil', 'maize',
        'mango', 'mothbeans', 'mungbean', 'muskmelon', 'orange', 'papaya',
        'pigeonpeas', 'pomegranate', 'rice', 'watermelon'
    ]
    
    recommended_crop = crops[crop_index]
    st.success(f"✅ Recommended Crop: **{recommended_crop.capitalize()}**")
