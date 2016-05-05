#!/usr/bin/env python

import csv
import StringIO


infile = open('/home/cloudera/Desktop/BigData/Value2008_full.csv', 'r')
outfile = open('/home/cloudera/Desktop/Value2008.csv', 'w')
attributes = []
for line in infile:
	line = line.strip()
	attributes = line.split(',')
	out = [attributes[1], ',', attributes[2], ',',attributes[9], ',', attributes[10], '\n']
	outfile.writelines(out)

