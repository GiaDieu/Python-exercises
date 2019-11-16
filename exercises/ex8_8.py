#!/usr/bin/env python3

__doc__ = '''
Viết script get_version nhận vào ngày ở format <month>/<day>/<year>.
VD: 03/28/16 làm parameter và in ra một version được tính theo quy luật sau:
- Version ở dạng format: <MAJOR>.<MINOR>.<PATCH>, vd: "6.9.2"
- Từ ngày 09 tháng 02 năm 2016, phiên bản bắt đầu là "1.0.0"
- Mỗi 28 ngày, MAJOR lại tăng thêm 1, MINOR và PATCH set về 0
- Mỗi tuần, MINOR tăng thêm 1 và PATCH sẽ set về 0
- Cứ mỗi ngày, PATCH lại tăng thêm 1.

Yêu cầu:
- Kiểm tra version thu được với lần lượt các input là "02/03/16", "09/06/16"
với thởi điểm cuối là "06/23/17"

Gợi ý: học viên sử dụng `sys.argv` hoặc module `argparse`
'''

import sys
import datetime


def get_version(input_data):
    '''Trả về tên phiên bản như yêu cầu tại ``__doc__``

    :param input_data: ngày format ở dạng <month>/<day>/<year>,
                       ví dụ: "02/03/16"
    :rtype str:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None
    start_time = datetime.datetime.strptime("02/09/16","%m/%d/%y")
    delta = datetime.datetime.strptime(input_data,"%m/%d/%y") - start_time
    days = delta.days
    MAJOR = days // 28 + 1
    MINOR = (days % 28) // 7
    PATCH = days % 7
    result = "{}.{}.{}".format(MAJOR, MINOR, PATCH)
    return result


def solve(input_data):
    '''Function `solve` dùng để `test`, học viên không cần chỉnh sửa gì thêm
    Chỉ thay đổi lại tên function của mình bên dưới cho phù hợp

    Gía trị trả về của hàm `solve` và `your_function` là như nhau

    :rtype str:
    '''
    result = get_version(input_data)
    return result


def main():
    input_data = sys.argv[1]
    print(solve(input_data))
    # sử dụng `sys.argv` hoặc `argparse` để gán gía trị yêu cầu
    # vào biến `input_data`
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa thực hiện truyền input_data")
    


if __name__ == "__main__":
    main()
