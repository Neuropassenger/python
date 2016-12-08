'''
Sample Input:
4
север 10
запад 20
юг 30
восток 40

Sample Output:
20 -20
'''

n = int(input())
commands = []
location = [0, 0]
for i in range(n):
	line = input().split()
	if line[0] == "север":
		location[1] += int(line[1])
	elif line[0] == "запад":
		location[0] -= int(line[1])
	elif line[0] == "юг":
		location[1] -= int(line[1])
	elif line[0] == "восток":
		location[0] += int(line[1])

print(location[0], location[1])



