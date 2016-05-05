#!/usr/bin/env python

infile = open('/home/cloudera/Desktop/BigData/Value2015_full.txt', 'r')
outfile = open('/home/cloudera/Desktop/Value2015.csv', 'w')
attributes = []
for line in infile:
	line = line.strip()
	attributes = line.split('\t')
	if(attributes[0] == ''):
		continue
	out = [attributes[1], '\t', attributes[2], '\t',attributes[12].replace(',',''), '\t', attributes[13], '\n']
	outfile.writelines(out)
