'''
Sample Input:
3
a
bb
cCc
2
a bb aab aba ccc
c bb aaa

Sample Output:
aab
aba
c
aaa
'''

d = int(input())
standard = []
for i in range(d):
	standard.append(str(input()).lower())

l = int(input())
text = []
for i in range(l):
	text.append(str(input()).lower().split())

wrong_words = []
for i in range(len(text)):
	for j in range(len(text[i])):
		if text[i][j] not in standard:
			if text[i][j] not in wrong_words:
				wrong_words.append(text[i][j])

for word in wrong_words:
	print(word)