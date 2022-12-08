from random import *
import os
import colorama
import random


def out_green(text):
    print("\033[1m\033[32m {}\033[0m".format(text))


def out_violet(text):
    print("\033[3m\033[35m {}\033[0m".format(text))


def out_blue(text):
    print("\033[1m\033[36m {}\033[0m".format(text))


def out_red(text):
    print("\033[31m{}".format(text))


text = """
 ██████╗ █████╗ ███╗   ██╗██████╗ ██╗   ██╗    ██████╗  █████╗ ████████╗████████╗██╗     ███████╗
██╔════╝██╔══██╗████╗  ██║██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
██║     ███████║██╔██╗ ██║██║  ██║ ╚████╔╝     ██████╔╝███████║   ██║      ██║   ██║     █████╗  
██║     ██╔══██║██║╚██╗██║██║  ██║  ╚██╔╝      ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
╚██████╗██║  ██║██║ ╚████║██████╔╝   ██║       ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝    ╚═╝       ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
                                                                                              
"""

bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in text.split('\n')]
print('\n'.join(colored_lines))

hello = '"Сладкая" игра для маленьких "сладкоежек"! Кто же выиграет, и сорвёт конфетный куш?!\n'
out_green(hello)

out_blue('Хочешь забрать всё? Тогда выйграй! \n')
rules = ('Правила просты: \n'
         '- Перед Вами 2021 конфета \n'
         '- Конфеты берёте по очереди \n'
         '- За раз можно взять не больше 28 конфет \n'
         '- Кто забрал последнюю - ПОБЕДИТЕЛЬ!')
out_violet(rules)

message = ['Руки-загребуки', 'Главное чтобы не слиплось', 'Бери больше шоколадных', 'Чем больше - тем лучше']


def player_vs_player():
    candies = 2021
    max_take = 28
    count = 0
    player_1 = input('\nКак зовут тебя "карамелька"? ')
    print(f'Привет {player_1}!')
    player_2 = input('\nТеперь время представится второй "конфетке"? ')
    print(f'Привет {player_2}!')

    print(f'\nМы просим от Вас честной игры {player_1} и  {player_2} !\n')
    print('Кто же будет первым?! Да решит же всё жребий!\n')

    lot = randint(1, 2)
    if lot == 1:
        win = player_1
        lose = player_2
    elif lot == 2:
        win = player_2
        lose = player_1
    print(f'{win} удачлив, ходи первым!')

    while candies > 0:
        if count == 0:
            round = int(input(f'{choice(message)} {win}! \n '))
            if round > candies or round > max_take:
                print(f'Кому-то не хватает сладкого? Можно взять {max_take}, давай сначала: ')
                continue
            else:
                candies = candies - round
        if candies > 0:
            print(f'Осталось ещё {candies} конфет, игра продолжается! \n')
            count = 1

        if count == 1:
            round = int(input(f'{choice(message)} {lose}! \n '))
            if round > candies or round > max_take:
                print(f'Кому-то не хватает сладкого? Можно взять {max_take}, давай сначала: ')
                continue
            else:
                candies = candies - round
        if candies > 0:
            print(f'Осталось ещё {candies} конфет, игра продолжается! \n')
            count = 0
    else:
        out_red('Наши сласти закончились')

    if count == 0:
        out_green(f'ПОБЕДИТЕЛЬ {win}')
    else:
        out_green(f'ПОБЕДИТЕЛЬ {lose}')


player_vs_player()

end = """
 ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
    """
bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
codes = vars(colorama.Fore)
colors = [codes[color] for color in codes if color not in bad_colors]
colored_lines = [random.choice(colors) + line for line in end.split('\n')]
print('\n'.join(colored_lines))


