from import_file import import_file_cols as im_f_cols
from import_file import import_row_file as im_f_row
from export_file import export_rows as ex_rows
from export_file import export_cols as ex_cols
import ui

def download_guide(a):
    if a == 'cols':
        in_list = im_f_cols()
        in_list1 = [i.replace('\n', '') for i in in_list]
        in_list1 = list(filter(None, in_list1))
        in_list2 = [in_list1[i:i+4] for i in range(0, len(in_list1), 4)]
    if a == 'rows':
        in_list = im_f_row().strip().replace('"', '').replace(' ', '').split('\n')
        in_list2 = [i.split(';') for i in in_list]
    print(in_list2, '\nСправочник выгружен. ')
    return in_list2


def upload_guide(a, massive):  # выгрузка в файл
    if a == 'col':
        ex_cols(massive)
    if a == 'row':
        ex_rows(massive)
    print('\nВсё хорошо справочник выгружен! ')
    
def run():
    temp = ui.choice_format()
    guide = download_guide(temp)
    temp = ui.next_operation()
    while temp[0] != 4:

        if temp[0] == 1 and temp[1] == 'cols':
            download_guide('cols')
            temp = ui.next_operation()

        if temp[0] == 1 and temp[1] == 'rows':
            download_guide('rows')
            temp = ui.next_operation()

        if temp[0] == 2 and temp[1] == 'cols':
            upload_guide('cols', guide)
            temp = ui.next_operation()

        if temp[0] == 2 and temp[1] == 'rows':
            upload_guide('rows', guide)
            temp = ui.next_operation()
        if temp[0] == 3:
            print(ui.add_note(guide))
            temp = ui.next_operation()