FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    r-base \
    openjdk-11-jdk \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app/notebooks

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]
