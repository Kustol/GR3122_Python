# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def find_coordinate(quarter):
    while quarter < 1 or quarter > 4:
        quarter = int(input(f'{quarter} - некорректное число. Введите число от 1 до 4: '))

    if quarter == 1:
        return ('x ∈ (0; +∞); y ∈ (0; +∞)')
    elif quarter == 2:
        return ('x ∈ (-∞; 0); y ∈ (0; +∞)')
    elif quarter == 4:
        return ('x ∈ (0; +∞); y ∈ (-∞; 0)')
    else:
        return ('x ∈ (-∞; 0); y ∈ (-∞; 0)')

quarter = int(input('Введите номер четверти: '))

print(find_coordinate(quarter))
