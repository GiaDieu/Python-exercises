#!/usr/bin/env python3

data = {'first_50': 1230, 'from_51_to_100': 1530, 'above_100': 1786}


def calculate_cost(usage, prices):
    '''Tính tiền điện (integer)
    với giá tiền cho bởi đề bài, số điện tiêu thụ `usage`
    '''
    if usage <= 50:
        result = usage * data['first_50']
    elif 51 < usage <= 100:
        result = (usage - 50) * data['from_51_to_100'] + (50*data['first_50'])
    else:
        result = (usage-100) * data['above_100'] + (50*data['from_51_to_100']) + (50*data['first_50'])
    
    return result


def solve(input_data):
    result = None
    # Bài này làm mẫu, gọi function học viên định nghĩa với input để
    # tính kết quả.
    # Các bài còn lại học viên tự định nghĩa function và gọi function để
    # tính toán kết quả `result`
    result = [calculate_cost(i, input_data['prices'])
              for i in input_data['usages']]

    return result


def main():
    '''
    Cho tiền điện sinh hoạt được tính theo công thức:

    - 50 số đầu: 1230 VND/số.
    - 50 số tiếp: 1530 VND/số.
    - Các số tiếp theo: 1786 VND/số.
    '''
    idata = {'usages': [1, 29, 1235, 69, 100], 'prices': data}
    print(solve(idata))


if __name__ == "__main__":
    main()
