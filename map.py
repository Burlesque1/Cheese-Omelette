#!/usr/bin/env python

import sys
import os

attributes = []
for line in sys.stdin:
	line = line.strip()
	attributes = line.split(',')
	if(attributes[0] == '' or attributes[0] == "vendor_name"):
		continue
	date, time = attributes[1].split(' ')
	hour, minute, second = time.split(':')
	try:
		hour = int(hour)
	except ValueError:
		continue
	if(8 <= hour <= 18):
		print("%d\t%s\t%s"%(hour, attributes[9], attributes[10]))
