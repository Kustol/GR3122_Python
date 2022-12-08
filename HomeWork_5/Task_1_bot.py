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

def player_vs_bot():
    candies = 2021
    max_take = 28
    count = 0
    player_1 = input('\nКак зовут тебя "карамелька"? ')
    print(f'Привет {player_1}!')
    player_2 = 'Ириска'
    players = [player_1, player_2]

    print(f'{player_2} приветствует игрока {player_1}\n')
    print('Кто же будет первым?! Да решит же всё жребий!\n')

    winner = randint(-1, 0)

    print(f'{players[winner + 1]} удачлив, ходи первым!')

    while candies > 0:
        winner = winner + 1

        if players[winner % 2] == 'Ириска':
            if candies < 29:
                round = candies  # забирает оставшиеся конфеты
            else:
                delenie = candies // 28
                round = candies - ((delenie * max_take) + 1)
                if round == -1:
                    round = max_take - 1
                if round == 0:
                    round = max_take
            while round > 28 or round < 1:
                round = randint(1, 28)
            print(round)
            if candies > 0:
                candies = candies - round
        else:
            round = int(input(f'{choice(message)}  {players[winner % 2]}! \n '))
            if round > candies or round > max_take:
                print(f'Кому-то не хватает сладкого? Можно взять {max_take}, давай сначала: ')
                continue
            else:
                candies = candies - round
        if candies > 0:
                print(f'Осталось ещё {candies} конфет, игра продолжается! \n')
    out_green(f'На кону осталось {candies} \nПобедил {players[winner % 2]}')

player_vs_bot()

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