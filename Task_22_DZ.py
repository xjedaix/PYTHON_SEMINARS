# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит в строку первый список затем на следующией строке второй список.

lst1 = input().split()
lst2 = input().split()
lst1 = [int(x) for x in lst1]
lst2 = [int(x) for x in lst2]
intersection = set(lst1) & set(lst2)
result = sorted(list(intersection))
print(result)
