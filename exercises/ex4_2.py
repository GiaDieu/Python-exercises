#!/usr/bin/env python3


def solve(octal):
    '''Trả về giá trị cần cộng thêm với octal để thu được 0o777

    Với người dùng Unix(Ubuntu, MacOS,...), mode của một file được biểu diễn ở
    dạng Octal, VD: 644, 400, 777...

    Gợi ý:

    In [1]: oct(73)
    Out[1]: '0o111'
    '''

    
    result = 0o777-octal
    return result


def main():
    print(solve(0o644))


if __name__ == "__main__":
    main()
