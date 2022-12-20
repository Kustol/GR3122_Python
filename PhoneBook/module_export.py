import view


def create_files(contact):
    with open('in_line.txt', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}; {contact[1]}; {contact[2]}; {contact[3]};\n')

    with open('list.csv', 'a', encoding='UTF-8') as file:
        file.write(
            f'{contact[0]}\n {contact[1]}\n {contact[2]}\n {contact[3]}\n')

def reading_file(param):
    r = view.output()
    if r == 1:
        with open('in_line.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                if param in line:
                    print(line)

    if r == 2:
        list = []
        with open('in_line.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                if param in line:
                    list = line.split(';')
                    print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n')


def read_all_contacts():
    r = view.output()
    if r == 1:
        with open('in_line.txt', 'r', encoding='UTF-8') as file:
            for line in file:
                print(line)
    if r == 2:
        with open('list.csv', 'r', encoding='UTF-8') as file:
            for line in file:
                print(line)
