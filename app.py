#!/usr/bin/env python
from influxdb import InfluxDBClient
import datetime
import sys
import time
import os
import requests


def output(msg):
    # Convenience function to always show a correct output
    now = datetime.datetime.now()
    print("%s ticker %s" % (now, msg))


if __name__ == '__main__':
    # Gather our settings
    influx_host = os.getenv('INFLUX_HOST', 'localhost')
    influx_port = os.getenv('INFLUX_PORT', '8086')
    influx_user = os.getenv('INFLUX_USER', 'root')
    influx_pass = os.getenv('INFLUX_PASS', 'root')
    # Create our connections
    # Check to make sure we can create a connection
    got_if_connection = False
    while not got_if_connection:
        output('Trying InfluxDB connection...')
        output("Influx host: %s" % influx_host)
        output("Influx port: %s" % influx_port)
        influx_client = InfluxDBClient(host=influx_host, port=influx_port,
                                       username=influx_user,
                                       password=influx_pass)
        try:
            influx_client.get_list_database()
        except requests.exceptions.ConnectionError:
            output('No InfluxDB connection yet. Waiting 5 seconds and '+
                   'retrying.')
            time.sleep(5)
        else:
            got_if_connection = True
