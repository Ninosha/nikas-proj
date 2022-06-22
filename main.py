import os
from google.cloud import bigquery
import time
from google.cloud import exceptions
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "key.json"
client = bigquery.Client()

limit_number = 2


def create_table():
    archived_table_id = "cedar-heaven-349107.yellow_taxi.archived_data"
    source_table_id = "cedar-heaven-349107.yellow_taxi.yellow_taxi_table"
    schema = client.get_table(source_table_id).schema
    try:
        table = bigquery.Table(archived_table_id, schema=schema)

        archived_table = client.create_table(table)
        print("table created")
    except Exception as error:
        print(f"{archived_table_id} table already exists")


def move_rows(rows_number, ids):
    # copy_sql = f"""
    # CREATE TABLE IF NOT EXISTS
    # cedar-heaven-349107.yellow_taxi.archived_data
    #  AS
    # SELECT
    #  *
    # FROM `cedar-heaven-349107.yellow_taxi.yellow_taxi_table`
    # ORDER BY tpep_pickup_datetime
    # ASC
    # LIMIT {rows_number - 1}"""
    copy_sql = f"""
    INSERT INTO `cedar-heaven-349107.yellow_taxi.archived_data`
    SELECT 
    * 
    FROM `cedar-heaven-349107.yellow_taxi.yellow_taxi_table` 
    ORDER BY tpep_pickup_datetime
    ASC
    LIMIT {rows_number-1}"""

    delete_sql = f"""
    DELETE FROM `cedar-heaven-349107.yellow_taxi.yellow_taxi_table` 
    WHERE ID 
    in ({ids});"""
    print(ids)
    copy = client.query(copy_sql)
    copy.result()
    print("table copied")
    delete = client.query(delete_sql)
    delete.result()
    print("rows from first table deleted")


def get_diff(limit_number):
    query_job = client.query(

        f"""
        SELECT
            ID, tpep_pickup_datetime
        FROM `cedar-heaven-349107.yellow_taxi.yellow_taxi_table`
        ORDER BY tpep_pickup_datetime
        ASC
        LIMIT {limit_number}
         """
    )

    results = query_job.result()
    rows_dict = dict(results)
    datetimes = rows_dict.values()
    id_list = rows_dict.keys()
    earliest = max(datetimes) - min(datetimes)
    minutes = divmod(earliest.total_seconds(), 60)
    if len(tuple(id_list)[:-1]) <= 1:
        return minutes, str(tuple(id_list)[:-1][0]).replace("(", "").replace(")", "")
    else:
        return minutes, str(tuple(id_list)[:-1][0]).replace("(", "").replace(")", "")


minutes, id_list = get_diff(limit_number)
minutes = minutes[1]
create_table()
while True:
    while minutes == 0:
        limit_number += 1
        print(limit_number)
        print(minutes)
        print(f"diff is less than minute {minutes}")
        minutes, ids = get_diff(limit_number)
        minutes = minutes[1]
    else:
        minutes, ids = get_diff(limit_number)
        minutes = minutes[1]
        print(f"diff is 1 or more minutes {minutes}")
        time.sleep(1)
        print(f"slept for {minutes} minutes")
        move_rows(limit_number - 1, ids)
