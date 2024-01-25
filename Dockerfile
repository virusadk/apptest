
# Use the official Python image as the base image
FROM python:3.8




# Set the working directory in the container
WORKDIR /apptest

# Copy the application files into the working directory
COPY . /apptest
ARG CACHEBUST=1 
# Install the application dependencies
RUN echo "$CACHEBUST" pip install --no-cache -r require.txt

# Define the entry point for the container
CMD ["python","line.py","manage.py","runserver"]
