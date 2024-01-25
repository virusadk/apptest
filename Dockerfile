FROM python:3.9
WORKDIR /apptest
COPY requirements.txt /apptest/requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "line.py"]
