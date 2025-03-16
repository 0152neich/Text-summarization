FROM python:3.11-slim-bullseye

# Set working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libmagic1 swig \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy dependencies list
COPY requirements.txt /app/

# Install Python dependencies with cache optimization
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt --timeout=200
