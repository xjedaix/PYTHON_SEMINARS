"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

Пример
Ввод: 17 -> Вывод: 1, 2, 4, 8, 16
После загрузки задания, вы можете проверить себя самостоятельно с помощью эталонного решения
"""

def powers_of_two(n):
    powers = []
    for k in range(0, float('inf')):
        power = 2 ** k
        if power <= n:
            powers.append(power)
        else:
            break
    return powers
n = int(input())
powers = powers_of_two(n)
print(*powers)
