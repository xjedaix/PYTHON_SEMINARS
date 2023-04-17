# list_1 = [] # создает пустой список
# list_1 = list() # тоже создает пустой список
# list_1 = [1, 2, 3, 8]
# print(*list_1) 

# for i in list_1:
#     print(i)

# print (len(list_1))
# print(list_1[3])

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8) # добавляет в конец списка 
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# # Удаление последнего элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # [12, 7, -1]
# print(list_1.pop) # -1
# print(list_1) # [12, 7]

# # Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# # Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]

#Кортежи->

# t = (1, 5, 3,) # пустой кортеж
# print(type(t))

# v = [1, 8, 9]
# print(type(v))
# v = tuple(v)
# print(v)
# print(type(v))

# a, b = 1, 2 # множественное присваивание

# a,b,c = v

# print(a, b, c)

# t = [1, 2, 3, 5,]

# for i in range(len(t)):
#     print(t[i])

# t[0] = 2

# print(t)

# Словари ->

# d = {} # Пустой словарь
# d = dict()
# d['q'] = 'qwerty'
# print(d)

# d['w'] = 'werty'
# print(d)

# colors = {'red', 'green', 'blue'}
# print(colors) #{'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue', 'gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue', 'gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) #{'green', 'blue', 'gray'}
# colors.clear() # {}
# print(colors) # set()

# Операции со множествами в Python
a = {1, 2, 3, 5, 8}