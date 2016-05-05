#!/usr/bin/env python

import csv
import StringIO


infile = open('/home/cloudera/Desktop/BigData/House2010_full.csv', 'r')
outfile = open('/home/cloudera/Desktop/House2010bk.csv', 'w')
attributes = []
for line in infile:
	csv_file = StringIO.StringIO(line)
	csv_reader = csv.reader(csv_file)
	for record in csv_reader:
		if record[0] == "Brooklyn":
			try:
				total = float(record[4].replace(',',''))
			except ValueError:
				continue
			try:
				vacant = float(record[9])
			except ValueError:
				continue
			if total == 0:
				vacant_rate = 0
			else:
				vacant_rate = vacant * 100 / total
			vacant_rate = "%f" % vacant_rate
			out = [record[3], '\t', record[4].replace(',',''), '\t' , record[9] , '\t', vacant_rate, '\n']
			outfile.writelines(out)

