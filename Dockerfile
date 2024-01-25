# Use the official Python image as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /apptest

# Copy the application files into the working directory
COPY . /apptest

# Install the application dependencies
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["line.py"]