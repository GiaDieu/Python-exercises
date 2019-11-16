#!/usr/bin/env python3


def mymap(func, iterable):
    '''
    `map` là một built-in function trong Python, nó nhận vào 1 function và 1
    iterable (list, tuple, str, ...), rồi trả về một iterable tương ứng, sau khi
    biến đổi mỗi phần tử của iterable đó bằng function được gọi::

      In [1]: map(abs, [-1, -3, 4, 5])  # abs trả về giá trị tuyệt đối của số
      Out[1]: <map at 0x1121db6d8>

      In [2]: list(map(abs, [-1, -3, 4, 5]))
      Out[2]: [1, 3, 4, 5]
    '''

    result = list(map(func,iterable))
    return result


def solve(input_data):
    result = None

    result = mymap(input_data['func'], input_data['data'])
    return result


def main():
    data = {'func': lambda x: x**2,
            'data': [1, 2, 3, 4]}
    print(solve(data))


if __name__ == "__main__":
    main()
