# 17. Дан список чисел.
# Определите, сколько в нем встречается различных чисел.
#сделать список из неповторяющихся чисел жлементов

nums = [1, 2, 3, 4, 1, 2]
print(set(nums))

# элементы которые встречаются 1 раз
uniq_nums = [i for i in nums if nums.count(i) == 1]
uniq_nums1 = []

for i in nums:
    if nums.count(i) == 1:
        uniq_nums1.append

print(uniq_nums)
print(uniq_nums1)