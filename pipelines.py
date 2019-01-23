class RabbitMQPipeline(object):


    def __init__(self, rabbitmq_host, rabbitmq_queue):
        self.host = rabbitmq_host
        self.queue = rabbitmq_queue

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            rabbitmq_host=crawler.settings.get('RABBITMQ_HOST'),
            rabbitmq_queue=crawler.settings.get('RABBITMQ_QUEUE')            
        )

    def open_spider(self, spider):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue, durable=True)

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=json.dumps(item, cls=ScrapyJSONEncoder), properties=pika.BasicProperties(delivery_mode = 2))
        return item
