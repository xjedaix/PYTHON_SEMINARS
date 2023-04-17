"""
Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть. 
Стороны монеты вводятся построчно или в одну строку, если умеете.
"""

def min_flips(coins):
    num_heads = coins.count(0)
    num_tails = coins.count(1)
    if num_heads < num_tails:
        return num_heads
    else:
        return num_tails

coins = list(map(int, input().split()))
min_flips_count = min_flips(coins)
print(min_flips_count)
