#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time


sensorPfade = ['28-01143f8976aa','28-01143f625baa','28-01143f7d25aa','28-01143d2fd7aa','28-01143d5252aa','28-01143f683aaa']
fileName = 'output.csv'

def leseSensor(sensorName) :
	pfad = '/sys/bus/w1/devices/' + sensorName + '/w1_slave'
	file = open(pfad, 'r')
	lines = f.readlines()
	file.close()
	return lines

try:
    while True :
    	try:
	        sensorWerte = []
			for pfad in sensorPfade:
				sensorWerte.append( leseSensor(pfad) )
			if 
			outputString = time.strftime('%H:%M:%S') + ';'

			for wert in sensorWerte:
				outputString = outputString + wert + ';'

			file = open(file, 'a')
			file.write(outputString)
			file.close()
		except (OSError, IOError) as e:
			print("I/O error({0}): {1}".format(e.errno, e.strerror))

except KeyboardInterrupt:
    # Programm wird beendet wenn CTRL+C gedrückt wird.
    print('Programm wird beendet.')
    sys.exit(0)
except Exception as e:
    print(str(e))
    sys.exit(1)
    