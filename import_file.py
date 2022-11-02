def import_file_cols():  # импортируем файл с записью столбцами
    with open('data_cols.csv', 'r') as file:
        data = file.readlines()
    return data

def import_row_file():  # импортируем файл с записью строками
    with open('data_rows.csv', 'r') as file:
        data = file.read()
    return data