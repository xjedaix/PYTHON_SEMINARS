# 9. По данному целому неотрицательному n
# вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        while n > 0:
            result *= n
            n -= 1
        return result

# Пример использования функции
n = 5 # Заданное значение n
result = factorial(n)
print(f"Факториал числа {n} равен {result}")
