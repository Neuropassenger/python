
# coding: utf-8

# In[2]:

a = 1
sum = 0
while a != 0:
    a = int(input())
    sum += a;
print(sum)


# In[15]:

a = int(input())
b = int(input())
d = 1
while d % a != 0 or d % b != 0:
    d += 1
print(d)


# In[19]:

while True:
    num = int(input())
    if num < 10:
        continue
    elif num > 100:
        break
    print(num)


# In[7]:

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('', end='\t')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()


# In[8]:

a = int(input())
b = int(input())
sum = 0
count = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        count += 1
print(float(sum / count))


# In[10]:

strGC = str(input())
strGC = strGC.upper()
count = strGC.count('G')
count += strGC.count('C')
print(count / len(strGC) * 100)


# # Slicing

# In[12]:

s = 'abcdefghijk'
print(s[3:6], end=' ')
print(s[:6], end=' ')
print(s[3:], end=' ')
print(s[::-1], end=' ')
print(s[-3:], end=' ')
print(s[:-6], end=' ')
print(s[-1:-10:-2], end=' ')


# In[ ]:

string = str(input())
count = 0
index = 0
while index < len(string) - 1:
    if string[index] == string[index + 1]:
        count += 1
    else:
        string = string.replace(string[index] * count, string[index] + str(count))
        count = 0
    index+ += 1
print(string)


# In[15]:

line = str(input())
newline = ''
count = 0
i = 0
while i < len(line):
    # нужно предотвратить выход за границу
    j = i
    while line[i] == line[j]:
        count += 1
        j += 1
        if j >= len(line):
            break
    # заменяем
    newline += line[i] + str(count)
    count = 0
    i = j
print(newline)
    


# In[16]:

myList = []
myList += 'Olga'
print(myList)


# In[17]:

numbers = [int(i) for i in input().split()]
sumN = 0;
for i in range(len(numbers)):
    sumN += numbers[i]
print(sumN)


# In[24]:

inNums = [int(i) for i in input().split()]
sumNums = []
if len(inNums) == 1:
    print(inNums[0])
else:
    for i in range(len(inNums)):
        if i == 0:
            sumNums.append(inNums[-1] + inNums[1])
        elif i == len(inNums) - 1:
            sumNums.append(inNums[-2] + inNums[0])
        else:
            sumNums.append(inNums[i - 1] + inNums[i + 1])
for i in range(len(sumNums)):
    print(sumNums[i], end=' ')


# In[36]:

nums = [int(i) for i in input().split()]
nums.sort()
count = 0
i = 0
while i < len(nums):
    j = i
    while nums[i] == nums[j]:
        count += 1
        j += 1
        if j >= len(nums):
            break
    if count > 1:
        print(nums[i], end=' ')
    i = j
    count = 0


# In[1]:

nums = []
nSum = 0
while True:
    num = int(input())
    nums.append(num)
    nSum += num
    if nSum == 0:
        break
qSum = 0
for i in range(len(nums)):
    qSum += nums[i] ** 2
print(qSum)


# In[7]:

size = int(input())
step = 0
flag = False
for i in range(1, size + 1):
    for j in range(i):
        print(i, end=' ')
        step += 1
        if step == size:
            flag = True
            break
    if flag:
        break


# In[9]:

lst = [int(i) for i in input().split()]
x = int(input())
flag = True
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        flag = False
if flag:
    print('Отсутствует')


# In[17]:

matrix = []
newMatrix = []
line = []
while True:
    line = [i for i in input().split()]
    if 'end' in line:
        break
    matrix.append(line)


# In[18]:

matrix


# In[19]:

matrix = []
newMatrix = []
line = []

# чтение входной матрицы matrix
while True:
    line = [i for i in input().split()]
    if 'end' in line:
        break
    matrix.append(line)
line = []

# создание новой матрицы newMatrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == len(matrix) - 1:
            r = -1
        else:
            r = i
        if j == len(matrix[i]) - 1:
            c = -1
        else:
            c = j
        line.append(int(matrix[i - 1][j]) + int(matrix[r + 1][j]) +
                   int(matrix[i][j - 1]) + int(matrix[i][c + 1]))
    newMatrix.append(line)
    line = []
    
# вывод новой матрицы newMatrix
for i in range(len(newMatrix)):
    for j in range(len(newMatrix[i])):
        print(newMatrix[i][j], end=' ')
    print()


# In[37]:

n = int(input())
matrix = [[0] * n for i in range(n)]
r = 0
c = -1
rSize = n
cSize = n - 1
direction = 'Right'
moves = n * 2 - 1
element = 1

# заполнение матрицы matrix спиралью
for i in range(moves):
    if direction == 'Right':
        for j in range(rSize):
            c += 1
            matrix[r][c] = element
            element += 1
        rSize -= 1
        direction = 'Down'
        
    elif direction == 'Down':
        for j in range(cSize):
            r += 1
            matrix[r][c] = element
            element += 1
        cSize -= 1
        direction = 'Left'
        
    elif direction == 'Left':
        for j in range(rSize):
            c -= 1
            matrix[r][c] = element
            element += 1
        rSize -= 1
        direction = 'Up'
        
    elif direction == 'Up':
        for j in range(cSize):
            r -= 1
            matrix[r][c] = element
            element += 1
        cSize -= 1
        direction = 'Right'

# вывод матрицы matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

