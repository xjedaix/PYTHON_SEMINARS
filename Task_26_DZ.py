# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        result = power(base, exponent // 2)
        return result * result
    else:
        result = power(base, (exponent - 1) // 2)
        return base * result * result

A = 3
B = 5
print(power(A, B))  # Output: 243

A = 2
B = 3
print(power(A, B))  # Output: 8
