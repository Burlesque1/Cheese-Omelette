#!/usr/bin/env python

import json
from shapely.geometry import Point, Polygon
import sys
import os

Districts = []

with open('Brooklyn.json' ,'r') as data_file:    
    data = json.load(data_file)
data_file.close()

for index in range(0, len(data["coordinate"])):
    Districts.append(Polygon(data["coordinate"][index]))

attributes = []
for line in sys.stdin:
	line = line.strip()
	attributes = line.split('\t')
	if(len(attributes) == 3):
		try:
			log = float(attributes[1])
		except ValueError:
			continue
		try:
			lat = float(attributes[2])
		except ValueError:
			continue
		point = Point(log, lat)
		for index in range(0, len(Districts)):
			if(Districts[index].contains(point)):
				log = "%f" % log
				lat = "%f" % lat
				print("%s\t%s" % (log, lat))
				break
			
			


