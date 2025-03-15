FROM python:3.11-slim-bullseye

# Set the working directory in the container
RUN apt-get update && apt-get install -y \
    libmagic1 swig wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt --timeout=200