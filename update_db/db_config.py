from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "mybucket"

client = InfluxDBClient(url="http://"+"influxdb"+":8086", token="my-super-secret-auth-token", org="myorg")

write_api = client.write_api(write_options=SYNCHRONOUS)


