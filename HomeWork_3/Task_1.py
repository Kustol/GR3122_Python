"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

# Вариант 1 (с заданным списком)

my_list = [2, 3, 5, 9, 3]
total = 0
for i in range(len(my_list)):
    if i % 2 != 0:
        total = total + my_list[i]
print(f'Список: {my_list}')
print(f'Сумма нечётных элементов списка: {total}')




# Вариант 2 (со списком от пользователя)

num = int(input('Введите количество элементов в списке: '))

def list(num):
    list = []
    for i in range(num):
        n = int(input('Введите элемент списка: '))
        list.append(n)
    return list

def sum_odd_el(res):
    total = 0
    for i in range(len(res)):
        if i % 2 != 0:
            total = total + res[i]
    return total

res = list(num)
print(f'Список: {res}')
print(f'Сумма нечётных элементов списка: {sum_odd_el(res)}')
