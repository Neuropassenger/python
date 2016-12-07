with open('dataset_3363_3.txt', 'r') as inf:
	d = {}
	for line in inf:
		wordList = line.lower().split()
		for i in range(len(wordList)):
		    if wordList[i] in d:
		        d[wordList[i]] += 1
		    else:
		        d[wordList[i]] = 1
        
maxValue = 0
for value in d.values():
    if maxValue < value:
    	maxValue = value

md = {}
for key, value in d.items():
	if value == maxValue:
		md[key] = value

print(md)

cKey = "No key"
for i in range(len(md)):
	for key, value in md.items():
		if cKey == "No key":
			cKey = key
		elif cKey > key:
			cKey = key
	print(cKey, md[cKey])
	del md[cKey]
	i -= 1
	cKey = "No key"