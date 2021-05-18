import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='host.docker.internal'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
        out = open("folder_to_write_to/output.txt", "a")
        out.write("%r" % body + "\n")
        out.close()

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
