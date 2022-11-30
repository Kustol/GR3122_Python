"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""


def fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def negafibonacci(n):
    if n in [1, 2]:
        return -1
    else:
        return negafibonacci(n + 2) - negafibonacci(n + 1)


n = int(input("Введите целое число: "))

fibo_list = []
for i in range(1, n + 1):
    fibo_list.append(fibonacci(i))

negfib_list = []
for i in range(-n, 1):
    negfib_list.append(negafibonacci(i))

print(negfib_list + fibo_list)

