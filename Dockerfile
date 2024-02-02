FROM ubuntu:22.04

RUN apt-get update
RUN apt-get install -y python3

COPY . /opt/srcdevox

RUN pip install -r /opt/srcdevox/requirements.txt
# python -m flask --app board run --port 8000 --debug
ENTRYPOINT FLASK_APP=/opt/devox flask run --port 8000 --debug