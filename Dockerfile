# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && \
    apt-get install -y firefox-esr wget && \
    wget -q https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz && \
    tar -xzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin && \
    rm geckodriver-v0.30.0-linux64.tar.gz && \
    pip install selenium

# Create a directory for the app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Python script
CMD ["python", "main.py"]