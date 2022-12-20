import module_add as ma
import module_export as me
import view as v
import module_search as ms

def start():
    choice = v.welcome()
    if choice == 1:
        print('Добавить нового абонента')
        contact = ma.get_contact()
        me.create_files(contact)

    elif choice == 2:
        print('Поиск абонента')
        contact = ms.find()
        me.reading_file(contact)
        start()
    elif choice ==3:
        print('Показать всех абонентов')
        me.read_all_contacts()


