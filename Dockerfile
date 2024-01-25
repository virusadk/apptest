FROM python:3.8
WORKDIR /apptest

COPY requirements.txt /apptest/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /apptest

CMD ["python", "line.py"]
