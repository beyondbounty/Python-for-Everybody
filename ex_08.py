# https://www.youtube.com/watch?v=-9TfJF2dwHI
# Look for lines that begin with 'From (space)' and extract the third word

fname = input("Enter file name: ")

try:
	fhand = open(fname)
except:
	print("File does not exist")
	quit()

for line in fhand:
	words = line.split()
	if line.startswith('From') and len(words) > 2:
		print(words[2])