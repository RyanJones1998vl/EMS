FROM python:3.8-slim-buster

WORKDIR /api
EXPOSE 5000
ENV FLASK_APP=app.py

RUN apt-get update
RUN apt install -y libgl1-mesa-glx

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "flask", "run" , "-h", "192.168.108.50"]