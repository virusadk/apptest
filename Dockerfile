FROM python:3.9
# Set the working directory in the container
WORKDIR /apptest
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy the application files into the working directory
COPY . /apptest
# Define the entry point for the container
CMD ["python" , "line.py"]
