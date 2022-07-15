from google.cloud import pubsub_v1
from real_time_app.log import logger
import base64
import json

project_id = "crawler-project-349107"
topic_id = "taxi_topic"


def publish_rows(data):
    print("data", data)
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_id)
    message = str.encode(str(data).replace("'", '"'), "utf-8")
    future = publisher.publish(topic_path, message)
    future.result()
    logger.info(f"Published rows to {topic_path}.")
