"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)*
многочлена и записать в файл многочлен степени k.

    *Пример:*

    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
    -  k=5 => 2*x^5 + 4*x^4 + 2*x^3 + 2*x^2 + 4*x + 5 = 0
"""

from random import randint

print('Чтобы сформировать многочлен степени k и записать в файл, введите степень k! ')
k = int(input("Введите степень k: "))

factor = []  # создаем список из рандомных чисел для уравнения (кол-во эл-ов зависит от степени: k+1)
for i in range(1, k + 2):
    factor.append(randint(1, 101))

result = []  # заполлняем список исходя из значения степени
for i in range(len(factor)):
    if k == 1:
        result.append(f'{factor[i]}*x+')
    elif k == 0:
        result.append(f'{factor[i]}')
    else:
        result.append(f'{factor[i]}*x^{k}+')
    k -= 1

result.append('=0')

with open('task_4.txt', 'w') as data:
    data.write(''.join(result))
data.close()
