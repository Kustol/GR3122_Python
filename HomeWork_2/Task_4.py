"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt в одной строке одно число.
"""

number = int(input("Введите число: "))

def list(number):
    list = []
    for i in range(-abs(number), abs(number) + 1):
        list.append(i)
    return list

list_num = list(number)

path = 'file.txt'
data = open(path, 'r')
mult = list_num[int(data.readline())] * list_num[int(data.readline(2))]
data.close()

print(f'Список элементов от -{number} до {number}: {list_num}')
print(f'Произведение элементов: {mult}')
