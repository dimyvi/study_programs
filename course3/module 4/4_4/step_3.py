from zipfile import ZipFile
import os

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    ans = {}
    for i in info:
        if i.file_size != 0:
            ans[i.compress_size/i.file_size] = i.filename
    a = min(ans)
    a_ans = ans[a]
    aaa = os.path.basename(a_ans)
    print(aaa)