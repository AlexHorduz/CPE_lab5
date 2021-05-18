import pika
import time
from datetime import datetime


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='host.docker.internal'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while(True):
    date = datetime.now()
    str_date = date.strftime("%d/%m/%Y %H:%M:%S")
    channel.basic_publish(exchange='', routing_key='hello', body=str_date)
    print(" [x] Sent " + str_date)
    time.sleep(3)
connection.close()
