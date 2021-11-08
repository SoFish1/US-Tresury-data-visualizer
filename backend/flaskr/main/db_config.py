from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import socket

bucket = "mybucket"

client = InfluxDBClient(url="http://"+"localhost"+":8086", token="my-super-secret-auth-token", org="myorg")

write_api = client.write_api(write_options=SYNCHRONOUS)


