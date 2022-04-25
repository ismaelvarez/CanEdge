FROM python:3.7.9
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN apt-get install git



RUN git clone https://github.com/CSS-Electronics/canedge-influxdb-writer.git /usr/app/src/canedge-influxdb-writer && cd /usr/app/src/canedge-influxdb-writer && git checkout v1.0.4

WORKDIR /usr/app/src/canedge-influxdb-writer

SHELL ["/bin/bash", "-c"]

RUN pip install -r requirements.txt

RUN pip install -r requirements.txt

RUN apt install ca-certificates

RUN update-ca-certificates --fresh

RUN export SSL_CERT_DIR=/etc/ssl/certs

COPY ./entrypoint.sh ./

ENTRYPOINT [ "./entrypoint.sh"]
