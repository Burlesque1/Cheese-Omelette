#!/usr/bin/env python

import csv
import StringIO


infile = open('/home/cloudera/Desktop/BigData/Race2010_full.csv', 'r')
outfile = open('/home/cloudera/Desktop/Race2010bk.csv', 'w')
attributes = []
for line in infile:
	csv_file = StringIO.StringIO(line)
	csv_reader = csv.reader(csv_file)
	for record in csv_reader:
		if record[0] == "Brooklyn":
			out = [record[3], '\t', record[4].replace(',',''), '\t' , record[5].replace(',',''), '\t' ,
					record[6].replace(',',''), '\t' ,record[7].replace(',',''), '\t' ,record[8].replace(',',''), '\n' ]
			outfile.writelines(out)

