"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

num = int(input("Введите натуральное число N: "))
i = 2  # первое простое число
list = []
first = num
while i <= num:  # делим на 2ку пока делится, если нет i увеличиваем на 1
    if num % i == 0:
        list.append(i)
        num = num // i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {first} приведены в списке: {list}")
