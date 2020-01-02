#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import time
from python_json_config import ConfigBuilder

file_name = 'output.csv'

builder = ConfigBuilder()
config = builder.parse_config('config.json')


def fake_lese_sensor(sensor_name):
    return str(23.3)


def lese_sensor(sensor_name):
    sensor_pfad = '/sys/bus/w1/devices/' + sensor_name + '/w1_slave'
    sensor_file = open(sensor_pfad, 'r')
    lines = sensor_file.readlines()
    sensor_file.close()
    return str(lines)

try:
    os.mkdir('logs')
except Exception as e:
    print(str(e))

try:
    while True:
        try:
            sensorWerte = []
            for sensor in config.sensoren:
                sensorWerte.append(lese_sensor(sensor['Id']))
            output_string = time.strftime('%Y-%m-%d %H:%M:%S')

            for wert in sensorWerte:
                output_string = output_string + ';' + wert

            print(output_string)
            output_string = output_string + '\n'
            log_file = open('logs/' + time.strftime('%Y%m%d') + '.csv', 'a')
            log_file.write(output_string)
            log_file.close()

        except (OSError, IOError) as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
        time.sleep(1)

except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
    print('Programm wird beendet.')
    sys.exit(0)
except Exception as e:
    print(str(e))
    sys.exit(1)
