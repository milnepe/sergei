#! /usr/bin/python
# zigbee_test.py
# Author: Pete Milne
# Date: 28-01-2013
# Version: 1.0
# Writes a single character to serial port passed as commandline parameter
# Usage: python zigbe_test.py <port> <character> 


import serial, sys

SERIALPORT = sys.argv[1]
CHARACTER = sys.argv[2]

try:
	ser = serial.Serial(SERIALPORT, 9600)
	print("OK")
except serial.SerialException:
	print("FAILED")
	sys.exit()

ser.write(CHARACTER)

ser.close()
