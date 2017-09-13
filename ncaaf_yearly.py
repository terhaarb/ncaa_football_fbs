#!/usr/bin/python3

print ('hello\n', end='')
ncaaf_input=open("ncaaf_2016.txt", "r")

for line in ncaaf_input:
	line=line.replace('\t', ',')
	line=line.split(",")
	if line[0]==('Rk'):
		print ('header', end='')

	#print (line, end='')

ncaaf_input.close()
