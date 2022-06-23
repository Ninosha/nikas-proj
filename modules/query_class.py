import time
from log import logger
from google.cloud import bigquery


class Queries:
    def __init__(self, source_table_id, archived_table_id):
        self.client = bigquery.Client()
        self.archived_table_id = archived_table_id
        self.source_table_id = source_table_id

    def create_table(self):
        schema = self.client.get_table(self.source_table_id).schema
        try:
            table = bigquery.Table(self.archived_table_id,
                                   schema=schema)

            self.client.create_table(table)
            logger.info("table was created")
        except Exception as e:
            logger.info(
                f"{self.archived_table_id} table already exists")

    def copy_rows(self, rows_number):
        copy_sql = f"""
        INSERT INTO `{self.archived_table_id}`
        SELECT 
        * 
        FROM `{self.source_table_id}` 
        ORDER BY tpep_pickup_datetime
        ASC
        LIMIT {rows_number}"""

        print("copying ", rows_number - 1, "rows")

        start_time_copy = time.time()

        copy = self.client.query(copy_sql)
        copy.result()
        end_copy = time.time()
        logger.info(
            f"{end_copy - start_time_copy}, while copying needs seconds")
        logger.info("table copied")

    def delete_rows(self, ids):

        delete_sql = f"""
        DELETE FROM `{self.source_table_id}` 
        WHERE ID 
        in ({ids});"""

        print("ids: ", ids)
        start_time_delete = time.time()
        delete = self.client.query(delete_sql)
        delete.result()
        end_delete = time.time()
        logger.info(
            f"{end_delete - start_time_delete}, while deleting needs "
            f"seconds")

        logger.info("rows from first table deleted")
