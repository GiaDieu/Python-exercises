#!/usr/bin/env python3


def solve(numbers):
    '''Tính tổng và tích của dãy số `numbers`

    Return một tuple (sum, product)
    Không sử dụng hàm `sum`
    '''
    s = 0
    p = 1
    for i in numbers:
        s = s + i
        p = p * i
    result = (s, p)
    return result


def main():
    # Cho list numbers chứa các giá trị từ -10 đến 10, trừ số 0.
    numbers = range(-10, 11)
    numbers = list(numbers)
    numbers.remove(0)

    print(solve(numbers))


if __name__ == "__main__":
    main()
