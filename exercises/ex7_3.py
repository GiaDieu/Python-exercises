#!/usr/bin/env python3
# import random
# def solve(N):
#     # '''
#     # Giả lập việc một người tiến lên hoặc lùi lại, biết ta có thể
#     # giả lập việc người này tiến hay lùi bằng:

#     # random.choice(True, False) # nếu quy ước True là tiến, False là lùi.

#     # Với N trường hợp, tính tỷ lệ người này tiến lên
#     # phía trước với mỗi trường hợp.

#     # Trường hợp 1: chỉ bước 1 bước
#     # Trường hợp 2: bước 2 bước
#     # ...
#     # Trường hợp N: bước N bước

#     # Output là list tỷ lệ người này tiến lên phía trước trong
#     # N trường hợp (ở dạng float, vd 50% là 0.5).

#     # Đối với học viên học data analysis, yêu cầu sử dụng thư viện numpy để làm.
#     # ''''
#     result = []
#     for i in range(1, N + 1):
#         count_steps = 0
#         for steps in range(i):
#             steps = random.choice([True,False])
#             if steps == True:
#                 count_steps = count_steps + 1
#                 result.append(count_steps * 100 / i)
#     return result
# def main():
#     print(solve(100))


# if __name__ == "__main__":
#     main()
import random


def solve(N):
    '''
    Giả lập việc một người tiến lên hoặc lùi lại, biết ta có thể
    giả lập việc người này tiến hay lùi bằng:

    random.choice(True, False) # nếu quy ước True là tiến, False là lùi.

    Với N trường hợp, tính tỷ lệ người này tiến lên
    phía trước với mỗi trường hợp.

    Trường hợp 1: chỉ bước 1 bước
    Trường hợp 2: bước 2 bước
    ...
    Trường hợp N: bước N bước

    Output là list tỷ lệ người này tiến lên phía trước trong
    N trường hợp (ở dạng float, vd 50% là 0.5).

    Đối với học viên học data analysis, yêu cầu sử dụng thư viện numpy để làm.
    '''
    result = []
    for _ in range(1, N+1):
        choices = [random.choice([0, 1]) for _ in range(0, N)]
        result.append(float(sum(choices)/N))
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    return result


def main():
    print(solve(100))


if __name__ == "__main__":
    main()