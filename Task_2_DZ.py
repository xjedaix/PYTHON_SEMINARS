"""""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""""
# 1 способ
num = int(input("Введите трехзначное число: "))
digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
sum_of_digits = digit1 + digit2 + digit3
print("Сумма цифр трехзначного числа", num, "равна", sum_of_digits)

# 2 способ
num = input('Введите число: ')
num_sum = 0
for i in num:
    num_sum += int(i)
print(num_sum)