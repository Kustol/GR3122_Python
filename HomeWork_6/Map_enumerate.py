"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

numbers = [2, 3, 5, 9, 3, 5, 7, 8, 9, 10]

numbers = [sum(v for i, v in enumerate(numbers) if i % 2 != 0)]
print(''.join(map(str, numbers)))