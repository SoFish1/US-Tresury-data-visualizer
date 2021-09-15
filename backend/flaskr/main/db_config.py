from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "mybucket"

client = InfluxDBClient(url="http://xxx.xxx.xxx.xxx:8086", token="my-super-secret-auth-token", org="myorg")

write_api = client.write_api(write_options=SYNCHRONOUS)


