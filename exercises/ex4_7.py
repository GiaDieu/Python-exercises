#!/usr/bin/env python3
def solve(year):
    '''Trả về tuple-2 chứa year và tên gọi can chi tương ứng. Các từ trong tên
    đề phải viết hoa các chữ cái đầu.

    Biết có 10 thiên can::

    ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']

    Và 12 địa chi::

    ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu',
    'tuất', 'hợi']

    Năm 2017 là năm "Đinh Dậu".
'''
    thien_can = ['giáp', 'ất', 'bính', 'đinh', 'mậu', 'kỷ', 'canh', 'tân', 'nhâm', 'quý']
    dia_chi = ['tý', 'sửu', 'dần', 'mão', 'thìn', 'tị', 'ngọ', 'mui', 'thân', 'dậu','tuất', 'hợi']

    can = thien_can[(year - 4 )% 10]
    chi = dia_chi[(year - 4 ) % 12]

    thien_dia = '{0} {1}'.format(can, chi).title()
    return (year,thien_dia)

def main():
    print("Năm {0} là năm {1}".format(*solve(1696)))
    print("Năm {0} là năm {1}".format(*solve(1988)))

if __name__ == "__main__":
    main()
