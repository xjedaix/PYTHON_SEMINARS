# def sum_numbers(n, y = 'hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     # print(summa)
#     return summa

# # sum_numbers(5)

# a = sum_numbers(5)
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q', 'e', '1'))
# print(sum_str('q', 'e', '1', 'r'))

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
# print(quick_sort([10, 5, 2]))



def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):  # здесь была исправлена ошибка
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list1)
print(list1) # [1, 1, 2, 2, 4, 5, 6, 7, 8, 9, 55]
