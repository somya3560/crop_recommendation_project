# Use the official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Streamlit-specific: Prevents asking for user input
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_PORT=8501 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    STREAMLIT_SERVER_HEADLESS=true

# Command to run Streamlit app
CMD ["streamlit", "run", "app.py"]
