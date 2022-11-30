"""
Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и
минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

def get_fractional_part(list): # метод получения списка десятой части элементов
    for i in range(len(list)):
        list[i] = round(list[i] % 1, 2)
    return list

def diff_max_min(list): # вычисление max и min
    max = list[0]
    min = list[0]
    for i in range(len(list)):
        if list[i] != 0: # условие добавлено для игнорирования дробной части целого числа, т.е 0
            if list[i] > max:
                max = list[i]
            elif list[i] < min:
                min = list[i]
    return (max-min)

float_list = [1.1, 1.2, 3.1, 5, 10.01]

print(f' {float_list} => {diff_max_min(get_fractional_part(float_list))}')
