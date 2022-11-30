"""
Напишите программу, которая найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

num = int(input('Введите количество элементов в списке: '))

def list(num):
    list = []
    for i in range(num):
        n = int(input('Введите элемент списка: '))
        list.append(n)
    return list


def mult_el(res):
    list_2 = []
    for i in range((len(res)+1)//2):
        list_2.append(res[i]*res[len(res)-1-i])
    return(list_2)

res = list(num)
print(f'Список: {res}')
print(f'Произведение пар чисел: {mult_el(res)}')
