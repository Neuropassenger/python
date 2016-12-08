'''
Sample Input:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output:
*d*%*d*#*d*
dacabac
'''

de_alpha_string = str(input())
en_alpha_string = str(input())
de_string = str(input())
en_string = str(input())

dic = {}
for i in range(len(de_alpha_string)):
	dic[de_alpha_string[i]] = en_alpha_string[i]

out_en_string = ''
for i in range(len(de_string)):
	out_en_string += dic[de_string[i]]

dic = {}
for i in range(len(en_alpha_string)):
	dic[en_alpha_string[i]] = de_alpha_string[i]

out_de_string = ''
for i in range(len(en_string)):
	out_de_string += dic[en_string[i]]

print(out_en_string)
print(out_de_string)