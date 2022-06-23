import os
import time
from log import logger
from modules.main_funcs import get_diff
from modules.query_class import Queries

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"

# vars
limit_number = 2
archived_table_id = "cedar-heaven-349107.yellow_taxi.archived_data"
source_table_id = "cedar-heaven-349107.yellow_taxi.yellow_taxi_table"

# query object
query_job = Queries(source_table_id, archived_table_id)

# gets difference
minutes, _ = get_diff(limit_number, query_job.client)

# creates table
query_job.create_table()

if __name__ == "__main__":
    while True:
        while minutes == 0:
            logger.info(f"diff is less than minute: {minutes}")

            limit_number += 1

            logger.info(f"limit_number raised to: {limit_number}")

            minutes, ids = get_diff(limit_number, query_job.client)

        else:
            logger.info(f"diff is 1 or more minutes {minutes}")

            minutes, ids = get_diff(limit_number, query_job.client)

            time.sleep(1)   # minutes * 60

            logger.info(f"slept for {minutes} minutes")

            # copy rows
            query_job.copy_rows(limit_number - 1)

            limit_number = 2
            # delete rows
            query_job.delete_rows(ids)


