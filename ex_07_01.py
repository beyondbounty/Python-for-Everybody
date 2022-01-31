# https://www.youtube.com/watch?v=il1j4wkte2E
# Write a program to read through a file and print the contents of the file (line by line) all in upper case. Executing the program will look as follows

fname = input("Enter file name: ")

try:
	fhand = open(fname)
except:
	print(fname,"does not exist.")
	quit()
	
for line in fhand:
	print(line.rstrip().upper())
	