from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    count = 0
    ls = zip_file.namelist()
    for i in ls:
        if '.' in i:
            count += 1
    print(count)
