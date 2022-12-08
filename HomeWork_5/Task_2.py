"""
Создайте программу для игры в ""Крестики-нолики"".
"""


def print_board(b): #метод печати двумерного массива
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            print(b[i][j], end='\t')
        print()
    print()


def CheckWins(b): # выйгрышные комбинации(строка - столбец)
    if (b[0][0] == 'X' and b[0][1] == 'X' and b[0][2] == 'X' or b[0][0] == '0' and b[0][1] == '0' and b[0][2] == '0' or
        b[1][0] == 'X' and b[1][1] == 'X' and b[1][2] == 'X' or b[1][0] == '0' and b[1][1] == '0' and b[1][2] == '0' or
        b[2][0] == 'X' and b[2][1] == 'X' and b[2][2] == 'X' or b[2][0] == '0' and b[2][1] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][0] == 'X' and b[2][0] == 'X' or b[0][0] == '0' and b[1][0] == '0' and b[2][0] == '0' or
        b[0][1] == 'X' and b[1][1] == 'X' and b[2][1] == 'X' or b[0][1] == '0' and b[1][1] == '0' and b[2][1] == '0' or
        b[0][2] == 'X' and b[1][2] == 'X' and b[2][2] == 'X' or b[0][2] == '0' and b[1][2] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X' or b[0][0] == '0' and b[1][1] == '0' and b[2][2] == '0' or
            b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X' or b[0][2] == '0' and b[1][1] == '0' and b[2][0] == '0'):
        return True
    else:
        return False

def tic_tak_toe():
    board_size = 3
    board = ['*'] * 3
    winner = 0
    row = 0
    column = 0
    step = ''
    for i in range(board_size): # печатаем таблицу для игры
        board[i] = ['*'] * board_size
    print_board(board)
    for i in range(9): #порядок ходов (всего 9 ходов)
        if i % 2 == 0:
            print('Ходит "X"')
            step = "X"
        else:
            print('Ходит "О"')
            step = "0"
        row = int(input('Введите номер строки: ')) - 1 #отнимаем один, так как счёт с 0
        column = int(input('Введите номер столбца: ')) - 1
        while int(row) < 0 or int(row) > 2 or int(column) < 0 or int(column) > 2 or board[row][column] != '*':
            print('\nВведите числа в диапазоне от 1 до 3(исходя из оставшихся ячеек: \n')
            row = int(input('Введите номер строки: ')) - 1
            column = int(input('Введите номер столбца: ')) - 1
        board[row][column] = step
        print()
        print_board(board)
        CheckWins(board)
        if CheckWins(board) == True:
            winner = step
            break
    if winner == 'X':
        print("-X- ПОБЕДИЛ!!!")
    elif winner == '0':
        print("-0- ПОБЕДИЛ!!!")
    else:
        print("\nНи вашим, ни нашим!")

text = """Добро пожаловать на самый зрелищный бой!
Крестики-Нолики!!!\n
Уведите детей от экранов и начнём!\n
Поле сражения 3 на 3
"""
print(text)
tic_tak_toe()


