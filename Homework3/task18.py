# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = 5
lst = [random.randint(1,10) for _ in range(n)]
print(lst)
x = int(input("Введите число: "))
min = lst[0]
for i in lst:
    if abs(i-x) < abs(min-x):
       min = i
print(min)
