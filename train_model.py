import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your CSV file
df = pd.read_csv('Enhanced_Crop_Data.csv')  # This file must be in the same folder

# Features and labels
X = df[['temperature', 'humidity', 'soil_moisture']]
y = df['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("✅ Model trained and saved as model.pkl")
