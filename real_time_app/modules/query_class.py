import time
from real_time_app.log import logger
from google.cloud import bigquery


class Queries:
    """
    Query class, contains functions to create, copy data, delete data
    from tables
    """

    def __init__(self, source_table_id, archived_table_id):
        """
        :param source_table_id: str
        :param archived_table_id: str
        """
        self.client = bigquery.Client()
        self.archived_table_id = archived_table_id
        self.source_table_id = source_table_id

    def create_table(self):
        """
        creates table if not exists

        :return: logs message
        """

        # get source table schema
        schema = self.client.get_table(self.source_table_id).schema
        print(schema)
        # create table out of source table schema
        try:
            table = bigquery.Table(self.archived_table_id, schema=schema)

            self.client.create_table(table)
            logger.info("table was created")

        except Exception as e:
            logger.info(f"{self.archived_table_id} table already exists")

    def copy_rows(self, rows_number):
        copy_sql = f"""
        INSERT INTO `{self.archived_table_id}`
        SELECT 
        * 
        FROM `{self.source_table_id}` 
        ORDER BY tpep_pickup_datetime
        ASC
        LIMIT {rows_number}"""

        start_time_copy = time.time()

        copy = self.client.query(copy_sql)
        copy.result()
        end_copy = time.time()
        logger.info(
            f"{end_copy - start_time_copy}, while copying needs seconds"
        )
        logger.info("table copied")

    def delete_rows(self, datetime_column, datetime_string):
        """
        deletes rows from archived table according to ids passed

        :param datetime_list: list
        :param datetime_column: str
        :return: logs info
        """

        delete_sql = f"""
        DELETE FROM `{self.source_table_id}` 
        WHERE {datetime_column} 
        IN ({datetime_string});"""

        start_time_delete = time.time()

        delete = self.client.query(delete_sql)
        delete.result()

        end_delete = time.time()

        logger.info(
            f"data deleted, time needed: " f"{end_delete - start_time_delete}"
        )
