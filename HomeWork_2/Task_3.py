"""
Задайте список из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

    *Пример:*

    - Для n = 3:  {1: 2, 2: 2.25 , 3: 2.37}
"""

from math import pow

num = int(input('Введите число: '))
n_list = {}
for i in range(1, num + 1):
    n_list[i] = round(pow((1 + (1 / i)), i), 2)

print(f'Список {num} чисел: {n_list}')
print(f'Сумма значений спика: {sum(n_list.values())}')