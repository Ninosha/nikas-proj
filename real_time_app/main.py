import os
import time
from log import logger
from real_time_app.modules.main_funcs import get_args
from real_time_app.modules.query_class import Queries
from modules.publish_message import publish_rows

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/home/ninosha/Desktop/projects/thd/key.json"

# vars
limit_number = 2
archived_table_id = "crawler-project-349107.yellow_taxi.archived_data"
source_table_id = "crawler-project-349107.yellow_taxi.yellow_taxi_table"
timestamp_column = "tpep_pickup_datetime"

# query object
query_job = Queries(source_table_id, archived_table_id)

# gets difference
diff, datetime_string, rows_dict = get_args(
    source_table_id, limit_number, timestamp_column, query_job.client
)

# creates table
query_job.create_table()

current_datetime_str = ""
current_rows_dict = {}

if __name__ == "__main__":
    while True:
        while diff == 0:
            logger.info(f"diff is less than minute: {diff}")

            # raises number of rows to check by one
            limit_number += 1

            logger.info(f"limit_number raised to: {limit_number}")

            # checks difference again
            diff, datetime_string, rows_dict = get_args(
                source_table_id,
                limit_number,
                timestamp_column,
                query_job.client,
            )

            current_datetime_str = datetime_string
            current_rows_dict = rows_dict

        # if diff between max and min datetime is more than one do this
        else:
            logger.info(f"diff is 1 or more minutes {diff}")

            time.sleep(1)  # minutes * 60

            logger.info(f"slept for {diff} minutes")

            limit_number = 2

            # delete rows

            query_job.delete_rows(timestamp_column, current_datetime_str)

            diff, datetime_string, rows_dict = get_args(
                source_table_id,
                limit_number,
                timestamp_column,
                query_job.client,
            )

            publish_rows(data=rows_dict)
