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

#сложные условия с помощью логических операторов, таких как and, or, not
# if condition1 and condition2: #выполнится когда оба условия  окажутся верными
#     #operator
# if condition3 or condition4: #выполнится, когда хотя бы одно из условий окажется верным
#     #operator

# пример ->
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Урал, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# # Цикл While (позволяет выполнить блок кода, пока условие является верным)->
# while condition
#     #opertor 1
#     #operator 2
#         #. . . 
#         #operator n

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa) # 9

# Управляющие конструкции: while-else
#while condition:
    #operator 1
    #operator 2
    #. . . 
    #operator n
#else:
    #operator n + 1
    #operator n +2
    #. . . 
    #operator n+ m
#блок else выполняется, когда основное тело цикла
#перестает работать самостоятельно.
#А разве кто-то может прекратить работу цикла?
#Если мы вспомним то в C#, то да и  это конструкция 
#break.

# пример->
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

#цикл for, функция range()
# В Python цикл for в основном используется для перебора значений 
# Пример использования цикла for:
# for i in enumeration:
#     # operator 1
#     # operator 2
#     # . . .
#     # operator n
# for i in 1, -2, 3, 14, 5
#     print(i)
# #1 -2 3 14 5

# range выдает значения из диапазона с шагом 1
# Если указано только одно число - от 0 до заданного диапазона 
# Если нужен другой шаг, третьим аргументов можно задать приращение 

# r = range(5) #0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # ----
# r = range(1, 10, 2) # 1 3 5 7
# r = range(100, 0, -20) #100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, - 20)
# for i in r:
#     print(i)
# # 100 80 60 40 20

# Цикл for, функция range()
# можно использовать цикл for() и со строками,
# так как у строк есть нумерация, такая же 
# как и у массивов, начинается с 0
# for i in 'qwerty''
# #q
# #w
# #e
# #r
# #t
# #y

# a = 'qwerty'
# print(a[2])

# a = 'qwerty'
# for i in a:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)


# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(len(text))
# print('еще' in text)
# print(text.lower())
# print(text.uper())
# print(text.replace('еще', 'ЕЩЕ'))

# text = 'СъЕШЬ еще этих МяГкИх французских булок'
# print(text[0])                         # с
# print(text[1])                         # ъ
# print(text[len(text)-1])               # к
# print(text[-5])                        # б
# print(text[:])                         # съешь еще этих мягких французских булок
# print(text[:2])                        # съ
# print(text[len(text)-2])               # ок
# print(text[2:9])                       # ешь еще
# print([6: -18])                        # еще этих мягких
# print(text[0:len(text):6])             # сеикакл
# print(text[::6])                       # сеикакл
# text = text[2:9] + text[-5] + text[:2] # . . .