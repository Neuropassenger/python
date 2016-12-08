with open('dataset_3363_4.txt', 'r') as inf:
	students = {}
	ouf = open('output.txt', 'a')
	for line in inf:
		data = line.strip().split(';')
		students[data[0]] = data[1:4]
		ouf.write(str(((int(data[1]) + int(data[2]) + int(data[3])) / 3)) + '\n')
	ouf.close()
	
aMath = 0
aPhys = 0
aRus = 0

for value in students.values():
	aMath += int(value[0])
	aPhys += int(value[1])
	aRus += int(value[2])

with open('output.txt', 'a') as ouf:
	ouf.write(str(aMath / len(students)) + ' ' + str(aPhys / len(students)) + ' ' + str(aRus / len(students)) + '\n')