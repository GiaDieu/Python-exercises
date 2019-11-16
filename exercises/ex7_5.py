#!/usr/bin/env python3

import os
import sys
def solve():
    '''Return tuple chứa
    - Đường dẫn tới code của module `os`
    - list chứa các attribute của os và sys
    - Số dòng trong module `os`

    Biết dir(object) sẽ trả về tất cả thuộc tính (attribute) của object đó.
    Module cũng là object.

    In [11]: import os

    In [12]: len(dir(os))
    Out[12]: 284
    '''

    os_source = sys.modules['os']
    attributes = set(dir(os)) & set(dir(sys))
    with open("C:\\\\Users\\\\Gia Dieu\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python35\\\\lib\\\\os.py") as f:
        content = f.read()
    f.close()
    num_lines_os = len(content.split('\n'))
    result = (os_source, attributes,num_lines_os)
    return result
def main():
    print(solve())

if __name__ == "__main__":
    main()
