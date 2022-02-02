# https://www.youtube.com/watch?v=PrhZ9qwBDD8
# Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

fname = input("Enter file name: ")

try:
	fhand = open(fname)
except:
	print("File does not exist")
	quit()

days = dict()

for line in fhand:
	words = line.split()
	if line.startswith('From') and len(words) > 2:
		day = words[2] 
		days[day] = days.get(day,0) + 1

for day,count in days.items():
	print(day,count)


