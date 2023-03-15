# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

a = int(input())
b = int(input())

def degree(a,b):
    if b == 1:
        return a
    return (a * degree(a, b - 1))

print(degree(a,b))
