#!/usr/bin/env python3

__doc__ = '''
Yêu cầu:
- Tìm và in ra tổng số dòng của mỗi loại file (kể cả thư mục con,
dựa vào phần mở rộng abc.py và xyz.py là cùng loại) khi thực hiện lệnh:

    ex8_9.py `duong_dan_toi_thu_muc`

- Mặc định là thư mục hiện tại: PATH = '.'

Gợi ý: sử dụng `os.walk` để duyệt vào thư mục con.

Yêu cầu nâng cao:
- Trong thư mục hiện tại nếu tìm thấy file là python module
in ra màn hình tên của các function trong đó

Gợi ý: sử dụng 2 module `inspect` và `importlib`
``from inspect import isfunction``
``from importlib import import_module``
'''

import os
import sys
from os.path import join,getsize
from inspect import isfunction,getmembers
from importlib import import_module
PATH = '.'


def your_function(input_data):
    '''Trả về `dict` chứa tổng số dòng của từng loại file trong thư
    mục hiện tại (bao gồm cả thư mục con) theo format:

        result = {
            ".py": 1234,
            ".txt": 5678,
            ...
        }

    Lưu ý:
    - Nếu file không đọc được, gán số dòng bằng 0

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = {}
    file_categories = {}
    function_list = []
    for root,dirs,files in os.walk(PATH):
        for file_name in files:
            full_path = os.path.join(root,file_name)

            line = 0
            with open(full_path,'rb') as f:
                content = f.read()
                for _ in content:
                    line = line + 1
            

            file_type = file_name[file_name.rfind('.'):]
            if file_type not in result and file_type not in file_categories:
                result[file_type] = line
                file_categories[file_type] = [full_path]
            else:
                result[file_type] += line
                file_categories[file_type].append(full_path)
    
            if root == '.' and file_type == '.py':
                print('functions in module {} are:'.format(file_name[:-3]))
                module = import_module(file_name[:-3])
                list_function = [name_function for name_function, type_function in getmembers(module) if isfunction(type_function)]
                print(list_function)

    return result

def solve(input_data):
    '''Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :param input_data: đường dẫn tới thư mục
    :rtype dict:
    '''
    result = your_function(input_data)
    return result


def main():
    # path = PATH  # thư mục hiện tại

    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu vào biến `path`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    try:
        path = sys.argv[1]
    except Exception as e:
        path = PATH
    print(solve(path))


if __name__ == "__main__":
    main()
