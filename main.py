import numpy as np
#import pandas as pd
import math as m
import random as r

#_____________Список________________

n = 2 #int(input('Разрядность: '))
A = []
B = []
for i in range(n):
    A.append([0] * n)
    B.append([1] * n)
print()

#____________Матрица и ее печать______________

print('Элементы матрицы по строчкам')
for row in range(n):
    for col in range(n):
        A[row][col] = int(input('>>> '))
print('Матрица ', n, 'x', n)


for row in range(n):
    for col in range(n):
        print('{0:2}'.format(A[row][col]), end=' ')
    print()
print()

#___________________________________________

V = [[1, 2, 3, 0, 0, 0, 0, 1, 2], [4, 9, 9, 3, 0, 4, 5, 6, 1]]
print(np.mat(V))

print('Количество столбцов, содержащих хотя бы один нулевой элемент: ', sum(0 in x for x in zip(*V)))
print('Номер строки, в которой находится самая длинная серия одинаковых элементов.', max((i, len(x) - len(set(x))) for i, x in enumerate(V, 1))[0])
