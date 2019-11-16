#!/usr/bin/env python3

__doc__ = '''
Viết một chương trình log ra 1 file:
- Ở level INFO, với message là "started" khi chương trình đã chạy
- Ở level ERROR, bắt exception xảy ra và log nội dung (message)
của exception (Exception tùy ý).
- Ở level DEBUG, với message "running" sau mỗi 1 s

- Sau 3s, log ra ở level INFO dòng "exiting..." rồi kết thúc chương trình.

Yêu cầu:
- Thực hiện ghi vào file theo format:
    ``%(levelname)s - %(message)s - %(asctime)s``
- Đọc thêm về `format logging` tại đây hoặc gg:
    https://docs.python.org/3/library/logging.html#logrecord-attributes
'''

import logging
import os
import time
import shutil


def logging_files(filepath):
    '''Trả về list chứa các dòng đọc từ file
    sau khi thực hiện logging vào file

    Thực hiện 2 yêu cầu:
    1. Logging vào file như yêu cầu tại ``__doc__``
    2. Sau đó mở lại file, đọc và trả về list chứa các dòng đọc được từ file

    :rtype list:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = []

    # Thực hiện logging như yêu cầu, viết code bên dưới
    logging.basicConfig(filename = filepath,level = logging.DEBUG,
                        format = '%(levelname)s - %(message)s - %(asctime)s')
    
    logging.info('started')

    try:
        print('thầy cho bài khó quá')
    except Exception as e:
        logging.error('error message')

    for i in range(3):
        logging.debug('running')
        time.sleep(1)
    logging.info('exciting')
    # Thực hiện đọc và mở lại file, gán result là list chứa các dòng đọc được
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # Thông báo sử dụng xong logging, flush hết dữ liệu ra output.
    logging.shutdown()
    with open(filepath) as f:
        for line in f:
            result.append(line)
        f.close()

    # Xoá file sau khi đã thực hiện xong yêu cầu
    # os.remove(filepath)

    return result


def solve():
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại tên function của mình cho phù hợp

    :rtype list:
    '''
    import tempfile
    fd, fn = tempfile.mkstemp()
    result = logging_files(fn)
    os.close(fd)
    os.remove(fn)

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
