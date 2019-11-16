#!/usr/bin/env python3

data = [
    {"name": "Hoang"},
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]
def solve(input_data):
    '''Trả về list các tuple chứa cặp tên học viên và bạn gái.
    Nếu không có girl_friend thì đặt giá trị đó bằng string rỗng.
    '''
    result = []
    myDict = {}
    for Dict in input_data:
        for key,value in Dict.items():
            if value == 'Duy' or value == 'Dai':
                myDict[value] = Dict['girl_friend']
            elif value == 'Hoang' or value == 'Tu':
                myDict[value] = ''

    for k,v in myDict.items():
        result.append((k,v))
    return result
def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    result = solve(students)  # NOQA
    # In ra màn hình tên học viên kèm tên bạn gái (nếu có)
    print(result)

if __name__ == "__main__":
    main()
