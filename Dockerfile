FROM python:3.10-alpine
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install json-decoder
RUN pip3 install "requests<3"
RUN pip3 install schedule expressvpn-python
WORKDIR /apptest
COPY requirements.txt /apptest/requirements.txt
RUN pip3 install --upgrade pip -r requirements.txt
COPY . .
# EXPOSE 8000
CMD ["python", "line.py"]
