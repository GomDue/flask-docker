FROM python:3.10.2-slim

COPY . /app
WORKDIR /app
RUN pip3 install flask 
ENTRYPOINT python app.py