import time

from visualization.log import logger


def insert_rows(client, archived_table_id, rows_to_insert):

    start_time_copy = time.time()

    errors = client.insert_rows_json(archived_table_id, rows_to_insert)
    if not errors:
        logger.info("New rows have been added.")
    else:
        logger.error(f"Encountered errors while inserting rows: " f"{errors}")

    end_copy = time.time()
    logger.info(f"{end_copy - start_time_copy}, while copying needs seconds")
    logger.info("table copied")
