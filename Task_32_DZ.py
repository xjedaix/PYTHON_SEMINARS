# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# Input:
# 1, 3, 7, 10, 5, 8
# 4
# 8
# Output:
# 2(7), 4(5), 5(8)


def find_indexes(nums, min_val, max_val):
    indexes = []
    for i in range(len(nums)):
        if min_val <= nums[i] <= max_val:
            indexes.append((i, nums[i]))
    return indexes

# Пример использования
nums = [1, 3, 7, 10, 5, 8]
min_val = 4
max_val = 8
result = find_indexes(nums, min_val, max_val)
for i, val in result:
    print(f"{i}({val})", end=" ")
# Вывод: 2(7) 4(5) 5(8)
