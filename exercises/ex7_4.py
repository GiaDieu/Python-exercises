
def solve(text):
    '''Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    '''
    my_list = []
    my_dict = {}
    for i in text:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict[i] + 1

    for k,v in my_dict.items():
        if v > 1:
            my_dict[k] = k + k + str(v)
            my_list.append(my_dict[k])
        else:
            my_dict[k] = k + str(v)
            my_list.append(my_dict[k])
    
    result = ''.join(sorted(my_list))
    return result

def main():
    print(solve('abbbccccdddd'))


if __name__ == "__main__":
    main()