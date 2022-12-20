def get_contact():
    print('Нажмите ~ в поле "Имя" после добавления абонента')
    contact = []
    while(True):
        name = input('Имя: ')
        if name == '~':
            break
        contact.append(name)
        surname = input('Фамилия: ')
        contact.append(surname)
        phone = input('Номер телефона: ')
        contact.append(phone)
        info = input('Описание: ')
        contact.append(info)
        print(f'Добавлен абонент: {contact}')
    return contact
