'''
Sample Input:
6	Вяххи	159
11	Федотов	172
7	Бондарев	158
6	Чайкина	153

Sample Output:
1 -
2 -
3 -
4 -
5 -
6 156.0
7 158.0
8 -
9 -
10 -
11 172.0
'''

data = {}
for i in range(1, 12):
	data[i] = '-'

with open('dataset_3380_5.txt', 'r') as inf:
	for line in inf:
		split_line = line.strip().split('\t')
		if data[int(split_line[0])] == '-':
			data[int(split_line[0])] = [split_line[2]]
		else:
			data[int(split_line[0])].append(split_line[2])

for i in range(1, 12):
	if data[i] != '-':
		av = 0
		for j in range(len(data[i])):
			av += int(data[i][j])
		av /= len(data[i])
		data[i] = av

for key, value in data.items():
	print(key, value)