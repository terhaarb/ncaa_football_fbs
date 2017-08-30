#!/usr/bin/python3
import mysql.connector as mariadb
import re

mariadb_connection = mariadb.connect(user='root', password='mariadb', database='ncaa_football')
#cursor = mariadb_connection.cursor(buffered=True)
cursor = mariadb_connection.cursor()

cursor.execute("select * from teams_id where team like '%Michigan%';")
for item in cursor:
	print (item)
#print (cursor, end='')

print ("hello")

weekly_file = open('ncaaf_2016_week1.txt', 'r')

team_line=0
for line in weekly_file:
	if 'team logo' in line:
		line_strip_front = line[11:]
		line_strip_end = line_strip_front.rstrip()
		line_csv = line_strip_end.replace('\t', ',')
		line_list = line_csv.split(",")
		team_name = line_list[0]
		regex = re.compile('[^a-zA-Z]')
		new_name=regex.sub(' ', team_name)
		line_list[0]=new_name.strip()
		#print (line_list, end='')
		
		#item_num=0
		#for item in line_list:
		#	if item.isdigit():
		#		val=int(item)
		#		line_list[item_num]=val
		#	item_num=item_num +1
		#print (line_list, end='')

		if team_line==0:
			output_line='('
		for item in line_list:
			if not item.isdigit():
				output_line=output_line+"'"+item+"', "
			else:
				output_line=output_line+item+", "
		


		#if team_name contains :
		#	team_name_list=team_name.split(" ")
		#print (new_name, end='')
		#print (line_team[0], end='')
		#print (line_team, end='')
		search_team=line_list[0]
		#cursor.execute('select * from teams_id where team like %s', (search_team,))
		#cursor.execute('select * from teams_id where team = "Ole Miss";')
		#print (cursor, end='')
		team_line=team_line + 1
		if team_line==2:
			output_line=output_line[:-2]+'), '
			print (output_line, end='')
			#print ('final\n', end='')
			team_line=0
		#print ('\n', end='')

weekly_file.close()


#print(line.replace(textToSearch, textToReplace), end='')
#import mysql.connector as mariadb

#mariadb_connection = mariadb.connect(user='python_user', password='some_pass', database='employees')
#cursor = mariadb_connection.cursor()

