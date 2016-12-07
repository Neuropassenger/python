with open('dataset.txt', 'r') as inf:
	eLine = inf.readline()

dLine = ''
letter = ''
number = ''
for i in range(len(eLine)):
	if "\n" in eLine[i] or (eLine[i] not in "0123456789" and i > 0):
		dLine += letter * int(number)
		letter = ''
		number = ''

	if eLine[i].isdigit():
		number += eLine[i]
	elif eLine[i].isalpha():
		letter = eLine[i]

with open('outset.txt', 'w') as ouf:
	ouf.write(dLine + "\n")