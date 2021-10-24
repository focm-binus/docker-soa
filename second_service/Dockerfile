FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN apt-get update && apt-get -y install iputils-ping

COPY ./requirements_v1.txt $pwd

RUN pip install --upgrade pip
RUN pip install -r requirements_v1.txt

COPY ./v1 /app/app

