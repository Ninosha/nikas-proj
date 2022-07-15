import pandas as pd
from google.cloud import pubsub_v1
import os
from visualization.log import logger
from modules.utils import insert_rows
from google.cloud import bigquery
from modules.visualize import map_locations, map_data
import json
import webbrowser

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/home/ninosha/Desktop/projects/thd/key.json"

project_id = "crawler-project-349107"
subscription_id = "taxi_topic-sub"
client = bigquery.Client()
current = []
archived_table_id = "cedar-heaven-349107.yellow_taxi.archived_data"


def callback(message: pubsub_v1.subscriber.message.Message):
    # print(message)
    data = message.data.decode("utf8")
    data = json.loads(data)
    # insert_rows(client, archived_table_id, data)
    map_data(data)
    message.ack()

    # return data


def subscribe_rows(project_id, subscription_id):
    subscriber = pubsub_v1.SubscriberClient()

    subscription_path = subscriber.subscription_path(
        project_id, subscription_id
    )
    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=callback
    )
    logger.info(f"Listening for messages on {subscription_path}..\n")

    with subscriber:
        streaming_pull_future.result()


print(subscribe_rows(project_id, subscription_id))
