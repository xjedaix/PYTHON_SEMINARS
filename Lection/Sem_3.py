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

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([10, 5, 2]))