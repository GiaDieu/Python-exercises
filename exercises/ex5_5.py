#!/usr/bin/env python3


data = ['Trang', 'Trung', 'Tien',
        'Dai', 'Duong', 'Dung', 'Hung', 'Huy', 'Hoang']


def solve(students, N=5):
    '''Biết những bạn có tên bắt đầu bằng chữ `D` sẽ ngồi phòng thi số N,
    các bạn có tên bắt đầu chữ `H` ngồi phòng thi số N+1, và các bạn còn lại,
    nếu có tên kết thúc là `ng` sẽ ngồi cùng phòng các bạn tên `H`, còn lại
    ngồi cùng phòng `D`.

    Trả về result là list các tuple chứa (tên học viên, phòng thi), sắp xếp
    theo thứ tự tên học viên.
    '''

    result = []
    my_dict = {}
    for names in students:
        if names[0] == 'D':
            my_dict[names] = N
        elif names[0] == 'H':
            my_dict[names] = N + 1
        elif names[-2:] == 'ng':
            my_dict[names] = N + 1
        else:
            my_dict[names] = N
    
    for k,v in my_dict.items():
        result.append((k,('phòng thi: %d' % v)))

    return result


def main():
    students = data
    # Cho danh sách học viên students
    print(solve(students))


if __name__ == "__main__":
    main()
