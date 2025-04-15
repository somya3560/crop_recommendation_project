# Use official Python image as a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py"]
