
# Use the official Python image as the base image
FROM python:3.8

DOCKER BUILD --no-cache


# Set the working directory in the container
WORKDIR /apptest

# Copy the application files into the working directory
COPY . /apptest

# Install the application dependencies
RUN pip install --no-cache -r require.txt

# Define the entry point for the container
CMD ["python","line.py","manage.py","runserver"]
