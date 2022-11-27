"""
Напишите программу, которая
принимает на вход число N и выдает набор произведений чисел от 1 до N.
"""

number = int(input("Введите число: "))

def factorial(number):
    total = 1
    for i in range(1, number + 1):
        total *= i
    return total

def print_line():
    print('[', end='')
    for i in range(1, number + 1):
        if i == number:
            print(f'{factorial(i)}', ']', sep='')
        else:
            print(f'{factorial(i)}', end=', ')

print(f'Набор произведений чисел от 1 до {number}: ', end='')
print_line()
