#!/usr/bin/env python3

'''
Input: một số nguyên trong range(1,13).
Output: tên tương ứng của tháng đó bằng tiếng Anh, và số ngày trong tháng đó.
Tháng 2 tính 28 ngày.

Ví dụ:

- input_data: 2

- output: February 28
'''


# def solve(input_data):
#     '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

#         input_data: 2
#         output: ("February", 28)

#     :param input_data: tháng bất kì
#     :rtype: tuple
#     '''
#     assert (input_data in range(1, 13)), "Tháng không tồn tại"
#     result = ('')
#     input_data = input_data - 1
#     month = ['january','february','march','april','may','june','july','august','september','october','november','december']
#     maxDay = [31,28,31,30,31,30,31,31,30,31,30,31]
#     for i in range(len(month)):
#         for j in range(len(maxDay)):
#             if input_data == i and input_data == j:
#                  result = (month[i], maxDay[j])
#     return result

# def main():
#     month, day = solve(2)
#     print(month, day)


# if __name__ == "__main__":
#     main()

def solve(input_data):
    '''Trả về 1 `tuple` chứa 2 phần tử, ví dụ:

        input_data: 2
        output: ("February", 28)

    :param input_data: tháng bất kì
    :rtype: tuple
    '''
    assert (input_data in range(1, 13)), "Tháng không tồn tại"

    result = ('')

    month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    date_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    input_data = input_data - 1
    for i in range(len(month_list)):
        for j in range(len(date_list)):
            if i == input_data and j == input_data:
                result = (month_list[i],date_list[j])
    return result
def main():
    month, day = solve(int(input()))
    print(month, day)


if __name__ == "__main__":
    main()
