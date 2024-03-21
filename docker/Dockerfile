FROM python:3.12.2

RUN mkdir /opt/jobs
RUN mkdir /opt/files

COPY requirements.txt /opt/

COPY jobs/* /opt/jobs/
COPY files/*.zip /opt/files/

RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
