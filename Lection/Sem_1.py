#Семинар 1


#print(5, 8, 6) # вывод через запятую
"""
int - целые числа
float - дробные числа
bool - логический тип данных (true/ false)
str - строка
"""

# n = None # (None - ничего)
# print(n)

# n = 'fdfdf' # строка

# print(n)

# n = 'fd\'fd'  #\ выводит ковычки
#
# print(n) #type вевысти тип переменной

# print(5)
# print(5)
# print(5)
# print(5)
# print(5)

# шаблоны для вывода строк ->
# a = 5 #int
# b = 5.89 #float
# c = 'hello' #str
# # print(f"{a} - {b} - {c}") #выводим все через f, {a} фигурные скобки обозначают что мы выводим переменные
# print("{} - {} - {}".format(a, b, c)) # в ковычках пишем строку которую хотим вывести 

# ввод данных ->
# print('Введите первую строку')
# a = input()
# print(a)

# print('Введите первое число: ') #первый способ
# a = input()
# #print(a)
# b = input('Введите второе число: ') #второй способ
# print(a, '+', b, '=', a+b)

# приведение к числу->

# c = 5.89
# print(c)
# print(type(c)) #int отбрасывает дробную часть
# c = str(c)
# print(c + 89)
# print(type(c))

# c = 1
# print(c)
# print(type(c)) #int отбрасывает дробную часть
# c = bool(c)
# print(c)
# print(type(c))

# print('Введите первое число: ') #первый способ
# a = int(input())
# #print(a)
# b = int (input('Введите второе число: ')) #второй способ
# print(a, '+', b, '=', a + b)

#округление чисел->

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3)) # 3 - после запятой это кол-во знаков которое мы хотим оставить

# i++ в C# ->
# iter = 2
# iter += 3  # iter = iter +3
# iter -= 4  # iter = iter - 4
# iter *= 5  # iter = iter * 5
# iter/= 5   # iter = iter / 5
# iter //= 5 # iter =  iter // 5
# iter %= 5  # iter = iter % 5
# iter **=5  # iter = iter ** 5

# a = 1 > 4
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 == 2
# print(a)

# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# if и отступы->

#if condition:
    #operator 1
    #operator 2
    #. . . 
    #operator n
#else:
    #operator n + 1
    #operator n + 2
    #. . . 
    #operator n + m

#еще один вариент использования операторов else-if -> в связке с elif (else if)

# if condition:
#     #operator
# elif condition2:
#     #operator
# elif condition3:
#     #operator
# else:
#     #operator