# rabbitmq-pipeline

Scrapy pipeline that sends items to RabbitMQ

# Usage

1. Add this `pipelines.py` file to your scrapy project folder.
2. Add the following lines to `settings.py` 

### settings.py

```
ITEM_PIPELINES = {
    '[myproject].pipelines.RabbitMQPipeline': 301,
}

RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'scapy_data'
```
