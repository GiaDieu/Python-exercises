#!/usr/bin/env python3


# def solve(text):
#     '''Kiểm tra text có phải là palindrome không.

#     Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
#     kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
#     String phải dài hơn 1 chữ cái.
#     Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

#     :rtype: bool
#     '''
#     result = text.lower().replace(' ','')
#     return result == result[::-1]

# def main():
#     print(solve('Able was I ere I saw Elba'))
#     print(solve('Able was I ere I saw Elba1'))

# if __name__ == "__main__":
#     main()

def solve(text):
    '''Kiểm tra text có phải là palindrome không.

    Một string được gọi là `palindrome` nếu viết xuôi hay ngược đều thu được
    kết quả như nhau (không phân biệt hoa thường, bỏ qua dấu space).
    String phải dài hơn 1 chữ cái.
    Ví dụ các palindrome: 'civic', 'Able was I ere I saw Elba', 'Noon'

    :rtype: bool
    '''
    text = text.lower().replace(' ','')
    return text == text[::-1]

def main():
    print(solve('Able was I ere I saw Elba'))
    print(solve('Able was I ere I saw Elba1'))
    print(solve('Civic'))
    print(solve('Race car'))

if __name__ == "__main__":
    main()
