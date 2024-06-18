from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    compress = 0
    size = 0
    for i in info:
        if not i.is_dir():
            size += i.file_size
            compress += i.compress_size
print(f'Объем исходных файлов: {size} байт(а)')
print(f'Объем сжатых файлов: {compress} байт(а)')
