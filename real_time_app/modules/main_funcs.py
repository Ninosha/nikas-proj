from real_time_app.modules.utils import *


def get_args(source_table, limit_number, datetime_column, client):
    results = get_data(source_table, limit_number, datetime_column, client)
    datetimes_list = list(results[datetime_column])[:-1]
    diff = get_diff(datetimes_list)
    datetime_string = datetime_string_for_query(datetimes_list)
    rows_dict = results.to_json(orient="records")
    return diff, datetime_string, rows_dict
