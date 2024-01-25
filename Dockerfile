# Use the official Python image as the base image
FROM python:3.10

RUN mkdir /apptest

RUN python pip3 install -r --no-cache-dir --only-binary require.txt
# Set the working directory in the container
WORKDIR /apptest

# Copy the application files into the working directory
COPY . /apptest

# Install the application dependencies


# Define the entry point for the container
CMD ["python","line.py","manage.py","runserver"]
