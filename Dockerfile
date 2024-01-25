# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /apptest

# Copy the application files into the working directory
COPY . /

# Install the application dependencies
RUN pip install -r --no-cache-dir --only-binary require.txt

# Define the entry point for the container
CMD ["python","line.py","runserver"]
