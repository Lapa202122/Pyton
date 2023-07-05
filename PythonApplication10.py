# -*- coding: cp1251 -*-

import random

m = int(input('m = '))

n = int(input('n = '))

matrix_1=[[random.randint(1, 11) for j in range(n)] for i in range(m) ]
print()
print('Matrix 1: ')
print()

for i in range(m):

 print(matrix_1[i])

matrix_2 = [ [ random.randint(1, 11) for j in range(n)] for i in range(m) ]


print()
print('Matrix 2: ')
print()

for i in range(m):

 print(matrix_2[i])

result = [[matrix_1[i][j] + matrix_2[i][j]  for j in range

(len(matrix_1[0]))] for i in range(len(matrix_1))]

print()
print("Matrix 1 + Matrix 2: ")
print()
for r in result:

 print(r)

