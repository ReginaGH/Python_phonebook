def choice_format():
    print("\nВыберите формат записи телефонного справочника:\n"
    "rows - запись всех параметров одного абронента в одну строку\n"
    "cols - запись каждого параметра в отдельный стобец\n")
    note_format = input('Введите rows или cols: ')
    return note_format

def add_note():
    note = []
    note.append(input('\nВведите Фамилию: '))
    note.append(input('\nВведите Имя: '))
    note.append(input('\nВведите номер телефона: '))
    note.append(input('\nВведите комментарий: '))       
    return note

def next_operation():
    n = int(input('Что делаем дальше?\n1-Снова загрузим справочник\n2-Выгрузим справочник\n3-Добавить абонента\n4-Закончим работу\nВыберите действие: '))
    note_format = ' '
    if n == 1:
        note_format = input('Как загружаем, строками (rows) или колонками (cols): ')
    elif n == 2:
        note_format = input('Как будем выгружать, строками (rows) или колонками (cols): ')
    elif n==3:
        note_format = input('Как будем выгружать, строками (rows) или колонками (cols): ')
    elif n == 4:
        print('Работа закончена.')
    return n, note_format