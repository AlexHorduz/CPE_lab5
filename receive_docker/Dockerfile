FROM rabbitmq

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get -y install python3-pip
RUN apt-get install rabbitmq-server -y

RUN pip3 install pika

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN mkdir folder_to_write_to


COPY start.sh /usr/src/app
COPY receive.py /usr/src/app
CMD ["./start.sh"]
