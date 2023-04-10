"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
    001001 -> yes
"""



ticket_number = input("Введите номер билета: ")
if len(ticket_number) != 6:
    print("Номер билета должен состоять из 6 цифр.")
else:
    first_half = int(ticket_number[:3])
    second_half = int(ticket_number[3:])
    sum_first_half = sum(int(digit) for digit in str(first_half))
    sum_second_half = sum(int(digit) for digit in str(second_half))
    if sum_first_half == sum_second_half:
        print("yes")
    else:
        print("no")
