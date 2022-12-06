"""
Задайте последовательность чисел. Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности.
"""
import random

list = []
for i in range(20):
    num = random.randint(0, 20)
    list.append(num)
print(list)

new_list = []

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)


list = [random.randint(0, 20) for i in range(20)]
print(list)
new_list = []
[new_list.append(i) for i in list if i not in new_list]
print(new_list)
