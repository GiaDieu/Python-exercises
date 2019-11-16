#!/usr/bin/env python3


def solve(N):
    '''Creates a list contains all integer (not string) digits
    of ten last digits of `2**N`.
    '''
    result = None
    string_list = list(str(2 ** N)[-10:])
    result = [int(i) for i in string_list]
    return result

def main():
    print(solve(1000))


if __name__ == "__main__":
    main()
