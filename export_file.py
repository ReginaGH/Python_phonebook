import csv

def export_cols(data):
    with open('phonebook_cols.csv','w') as file:
        for i in range(0, len(data)):
            for j in range(0,4):
                print(data[i][j])
                file.write(f'{data[i][j]} \n')
            file.write(f'\n')

def export_rows(data):
    with open('phonebook_rows.csv', 'w') as file:
        for i in range(len(data)):
            line = ''
            for j in range(0,4):
                line += data[i][j] + ';'
            line = line[:-1]
            print(line)
            file.write(f'"{line}"\n')          
            