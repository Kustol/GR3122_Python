"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11

"""

number = float(input("Введите вещественное число: "))

def sum_digit(number):
    if number < 0:
        number = number * -1
    sum_num = 0
    for i in str(number):
        if i != '.':
            sum_num += int(i)
    return sum_num

print(f'Сумма цифр числа {number} равна {sum_digit(number)}')
