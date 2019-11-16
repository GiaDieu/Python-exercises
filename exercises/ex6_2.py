#!/usr/bin/env python3


def your_function(iterable, N):
    # Sửa tên, set giá trị return
    pass
def solve(iterable, N):
    ''' Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    '''
    lst1 = [iterable[i] for i in range(0,len(iterable),N)]
    lst2 = [iterable[j] for j in range(1,len(iterable),N)]
    result = [k for k in zip(lst1,lst2)]   
    # sửa thành tên function phù hợp
    # result = your_function(iterable, N)
    return result

def main():
    li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
    print(solve(li, 2))

if __name__ == "__main__":
    main()