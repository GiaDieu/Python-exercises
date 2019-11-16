#!/usr/bin/env python3


__doc__ = '''
Yêu cầu:
- Viết chương trình cứ 1 giây in ra màn hình thời gian hiện tại.
- Sau N lần thì chương trình kết thúc

Gợi ý:
time.sleep, datetime.datetime.now
'''

import time
import datetime # NOQA


def evaluate_current_time(N):
    '''Trả về tuple chứa 2 phần tử bao gồm:
    - List chứa các điểm thời gian (string) sau N lần thực hiện
    theo yêu cầu từ ``__doc__``
    - Tổng thời gian chạy của function

    :rtype tuple:
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    start = time.time()
    result = []
    for i in range(N):
        time.sleep(1)
        current_time = datetime.datetime.now()
        result.append(str(current_time))
        if i == N:
            break
    
    end = time.time()
    total_time = end - start
    return (result, total_time)


def solve(N):
    '''Học viên không cần chỉnh sửa trong hàm solve, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    Hàm solve dùng cho mục đích `test`
    :rtype tuple:
    '''
    result = evaluate_current_time(N)
    return result


def main():
    print(solve(5))


if __name__ == "__main__":
    main()
