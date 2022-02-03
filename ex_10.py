# https://www.youtube.com/watch?v=EhQxwzyT16E
# Make a list of the most common words and sort by values, instead of by the key

#fname = input("Enter file name: ")
fname = "mbox-short.txt"

try:
	fhand = open(fname)
except:
	print("File does not exist")
	quit()

counts = dict()

for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1
		
lst = list()

for k,v in counts.items():
	newtup = (v,k)
	lst.append(newtup)

lst = sorted(lst,reverse=True)

for v, k in lst[:5]:
	print(k,v)