FROM python:3.10.2-slim

ARG GDRIVE_SERVICE_ACCOUNT_JSON

COPY . /app
WORKDIR /app

RUN pip install "dvc[gdrive]"
RUN pip3 install flask 

RUN dvc init --no-scm -f

RUN dvc remote add -d storage gdrive://1Dsg1rRmK_ea2KbOEACEdlHGzRnebsMuA
RUN dvc remote modify storage gdrive_use_service_account true
RUN dvc remote modify storage gdrive_service_account_json_file_path GDRIVE_SERVICE_ACCOUNT_JSON

RUN dvc pull 

ENTRYPOINT python app.py
