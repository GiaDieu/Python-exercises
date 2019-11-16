data = '''Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments.''' # NOQA


def solve(input_data):
    '''
    Đặt result bằng list chứa 10 tuple ứng với 10 từ xuất hiện nhiều nhất,
    mỗi tuple chứa từ và số lần xuất hiện tương ứng.
    (Nếu có nhiều từ cùng xuất hiện với số lần như nhau thì trả về từ nào
    cũng được).
    '''
    result = []
    my_dict = {}
    new_string = ''
    for chars in input_data.lower():
        if chars != ',' and chars != '.' and chars != ';' and chars != '”' and chars != '“':
            new_string = new_string + chars
    new_string = new_string.replace("can’t","cannot")
    
    for words in new_string.strip().split(' '):
        if words not in my_dict:
            my_dict[words] = 1
        else:
            my_dict[words] = my_dict[words] + 1
    for k,v in my_dict.items():
        result.append((k,v))
    return sorted(result,key = lambda x: (x[1],x[0]),reverse = True)[0:10]

def main():
    result = solve(data)
    # In ra 10 từ xuất hiện nhiều nhất kèm số lần xuất hiện
    #
    # Viết code in ra màn hình sau dòng này
    print(result)


if __name__ == "__main__":
    main()