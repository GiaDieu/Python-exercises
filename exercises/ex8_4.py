#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Viết decorator in ra thời gian chạy của 1 function
'''

import time


def time_starts_stops(function):
    '''Tính thời gian chạy của `function` (float)
    '''
    time_start = time.time()
    function()
    time_stop = time.time()
    print(time_stop - time_start)
    return function

# Sửa tên decorator cho phù hợp
@time_starts_stops
def worker():
    for i in range(10000):
        pass
    time.sleep(1)


def solve():
    '''Thực hiện 1 tính toán bất kì trong function `solve`

    Trả về kết quả tùy ý, gán lại vào `result`
    '''
    result = worker()
    result = 5-2
    return result


def main():
    print("Function worker chạy mất: {0} giây".format(solve()))


if __name__ == "__main__":
    main()
