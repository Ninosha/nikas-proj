def datetime_string_for_query(datetimes_list):

    datetime_to_utc = map(
        lambda datetime: datetime.strftime("%Y-%m-%d %H:%M:%S UTC"),
        datetimes_list[:-1],
    )

    datetime_string = f"{list(datetime_to_utc)}".replace("[", "").replace(
        "]", ""
    )

    return datetime_string


def get_diff(datetimes_list):
    # getting difference between max and min datetimes
    diff = max(datetimes_list) - min(datetimes_list)

    # converting difference in minutes
    diff_minutes = divmod(diff.total_seconds(), 60)
    print(diff_minutes)
    return diff_minutes[1]


def get_data(source_table, limit_number, datetime_column, client):
    """
    function gets difference between maximum and minumum timestamps
    :param datetime_column: str
    :param limit_number: int/number on how many rows should query select
    :param client: obj/client
    :return: float/difference in minutes,
             str/strgified ids list for query
    """
    query_job = client.query(
        f"""
        SELECT
            *
        FROM `{source_table}`
        ORDER BY {datetime_column}
        ASC
        LIMIT {limit_number}
         """
    )
    result = query_job.result().to_dataframe()

    return result
