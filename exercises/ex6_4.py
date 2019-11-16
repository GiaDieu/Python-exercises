#!/usr/bin/env python3


def sumall(*input_data):
    '''Viết function ``sumall`` tính tổng của tất cả các số argument (int) được
    gọi. Thay input_data bằng code phù hợp.
    '''
    return sum(input_data)
    pass
    
def solve():
    result = None
    # # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Học viên chưa làm bài này")
    result = sumall(1, 2, 3, 4, 5, 6)
    return result

def main():
    print(solve())

if __name__ == "__main__":
    main()