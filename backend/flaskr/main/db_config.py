from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from os import environ


db_host_name = environ["DB_HOST_NAME"]
bucket = environ["DB_BUCKET_NAME"]
db_port = environ["DB_PORT"]
db_token = environ["DB_TOKEN"]
db_org = environ["DB_ORG"]

client = InfluxDBClient(url="http://"+db_host_name+":"+db_port, token=db_token, org=db_org)

write_api = client.write_api(write_options=SYNCHRONOUS)


