
FROM ubuntu:20.04
RUN apt-get update && apt-get install -y python3.9 python3.9-dev python-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python"]

FROM python:3.9
# Set the working directory in the container
WORKDIR /apptest
# Copy the application files into the working directory
COPY . /apptest
# Define the entry point for the container
CMD ["line.py"]
