n = int(input())
games = []
for i in range(n):
	games.append([i for i in input().split(';')])

team = {}
for game in games:
	if game[0] not in team:
		team[game[0]] = [0, 0, 0, 0, 0]
	if game[2] not in team:
		team[game[2]] = [0, 0, 0, 0, 0]
	team[game[0]][0] += 1
	team[game[2]][0] += 1
	if game[1] == game[3]:
		team[game[0]][2] += 1
		team[game[2]][2] += 1
		team[game[0]][4] += 1
		team[game[2]][4] += 1
	elif game[1] > game[3]:
		team[game[0]][1] += 1
		team[game[2]][3] += 1
		team[game[0]][4] += 3
	else:
		team[game[2]][1] += 1
		team[game[0]][3] += 1
		team[game[2]][4] += 3

for key, value in team.items():
	print(str(key) + ":" + str(value[0]), value[1], value[2], value[3], value[4])