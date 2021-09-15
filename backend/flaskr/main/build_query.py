from datetime import time
from .db_config import client




def build_query(fieldname,since_year,tag, time_opt="" ):
    
    query_mockup = 'from(bucket:"mybucket") '\
        '|> range(start: -Yy) '\
        '|> filter(fn: (r) => r["_measurement"] == "Treasury_data")'\
        '|> filter(fn: (r) => r["_field"] == "__FIELD__")'\
        '|> filter(fn: (r) => r["tag"] == "__TAG__")'


    if time_opt == "":
        query=query_mockup.replace("__FIELD__",  fieldname )
    elif time_opt == "y":
        query=query_mockup.replace("__FIELD__",  "y_"+fieldname )
    query=query.replace("-Yy", "-" + str(since_year) + "y")
    query=query.replace("__TAG__",  tag )
    data_frame = client.query_api().query_data_frame(query)

    return data_frame


# query=build_query("Total Withdrawals (excluding transfers)",1)


# data_frame = client.query_api().query_data_frame(query)

def get_last_fields(tag):
    query = 'from(bucket:"mybucket") '\
                '|> range(start: -1y) '\
                '|> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value") '\
                '|> filter(fn: (r) => r.tag == "__TAG__" )'\
                

    query=query.replace("__TAG__",  tag )
    
    last_data = client.query_api().query_data_frame(query)
    
    last_fields=last_data.head().columns.tolist()
    
    reduntant_fields=["result","table","_time","_start","_stop","_measurement","tag"]
    for field in reduntant_fields:
        try:
            last_fields.remove(field)

        except ValueError as e:
            print(e)
            

    return last_fields




