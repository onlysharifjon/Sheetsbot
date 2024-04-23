import openpyxl

# Load the Excel file

import os




def read_excel_part1(path, file_name):
    teachers = []
    all_data = []
    wb = openpyxl.load_workbook(path)
    ws = wb.active
    b_values = [ws.cell(row=i, column=2).value for i in range(2, ws.max_row + 1)]
    for value in b_values:
        all_data.append(str(value))
        if value is not None and str(value).strip() not in teachers:
            a = str(value).strip()
            teachers.append(a)
    for i in teachers:
        print(i)
    txt = ''
    for i in teachers:
        count = 0
        teacher_name = i
        for k in all_data:
            if i in k:
                count += 1
        print(teacher_name, ':', count)
        txt += f"👨‍🏫{teacher_name}: {count}🎓\n"

    os.remove(f'uploads/{file_name}')
    wb.close()
    return txt

