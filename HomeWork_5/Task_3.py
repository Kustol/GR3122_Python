"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Пример: "bbbcccaaaarrrrrr"
        "3b3c4a6r"
"""

def rle_compress(string):
    result = ''
    prev_symbol = ''
    count = 1
    if not string:
        return ''
    for i in string:
        if i != prev_symbol:
            if prev_symbol:
                result += str(count) + prev_symbol
            count = 1
            prev_symbol = i
        else:
            count += 1
    result += str(count) + prev_symbol
    return result

def rle_decompress(string):
    result = ''
    count = ''
    for i in string:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result


def compress():
    with open('Decompress.txt', 'w') as file:
        file.write(input('Напишите текст необходимый для сжатия: '))
    with open('Decompress.txt', 'r') as file:
        text = file.readline()
        text_compress = text.split()

    print(f'Было - {text}')
    text_compress = rle_compress(text)

    with open('Compress.txt', 'w') as file:
        file.write(f'{text_compress}')
    print(f'Стало - {text_compress}')

compress()

def decompress():
    with open('Compress.txt', 'w') as file:
        file.write(input('Напишите текст необходимый для восстановления: '))
    with open('Compress.txt', 'r') as file:
        text = file.readline()
        text_decompress = text.split()

    print(f'Было - {text}')
    text_decompress = rle_decompress(text)

    with open('Decompress.txt', 'w') as file:
        file.write(f'{text_decompress}')
    print(f'Стало - {text_decompress}')

decompress()


# src = [1, 1, 2, 1, 3, 5, 6, 3, 7, 7, 5, 4, 5, 4, 3, 1]
#
#
# def rle(src):
#     result = []
#     if src:
#         current = src.pop(0)
#         counter = 1
#         for e in src:
#             if e == current:
#                 counter += 1
#             else:
#                 result.append((counter, current))
#                 current = e
#                 counter = 1
#         result.append((counter, current))
#     return result
#
#
# print(rle(src))
