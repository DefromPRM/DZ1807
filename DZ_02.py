# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# n = int(input("Введите количество монеток: "))
# heads = 0
# tails = 0
# for i in range(n):
#     v = int(input("Орел - введите 1. Решка - введите 2: "))
#     if v == 1: heads += 1
#     else: tails += 1
# if heads < tails: print(f"Количество монеток, которые нужно перевернуть: {heads}")
# elif heads == tails: print(f"Количество монеток одинаковое")
# else: print((f"Количество монеток, которые нужно перевернуть: {tails} "))

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# from random import randint

# x = randint(1, 1001)
# y = randint(1, 1001)
# s = x + y
# p = x * y
# x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
# print(f'Петя загадал числа {x1}, {y1}')

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input("Введите число N: "))
# p = 1
# while p <= n:
#     print(p, end = ', ')
#     p = p*2

