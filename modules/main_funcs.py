def get_diff(limit_number, client):
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

    print(rows_dict)

    date_times = rows_dict.values()
    id_list = list(rows_dict.keys())
    ids_string = ", ".join(map(str, id_list[:-1]))
    diff = max(date_times) - min(date_times)
    diff_minutes = divmod(diff.total_seconds(), 60)
    return diff_minutes[1], ids_string
