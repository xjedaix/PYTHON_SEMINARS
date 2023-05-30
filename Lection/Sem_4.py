# def f(x):
#     return x*x
# a = f
# print(a(5))
# print(f(5))

# def calk1(a, b):
#     return a+a

# def calk2(a):
#     return a*a

# def math(op, x):
#     print(op(x))

# math(calk2, 5)

# data = [1, 2, 3, 5, 8, 15, , 23, 28]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

# def select(f, col):
#     return[f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 28]

# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = select(lambda x:(x, x**2), res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# //////////////////////

# data = '15 156 96 3 5 8 52 5'
# data = list(map(int, data.split()))
# print(data)

#///////////////

data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)