#!/usr/bin/env python3


def solve(N):
    '''Creates a list like this by listcomps::

      ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN]

    '''

    result = [str(i) * 6 for i in range(N) if i % 2 != 0]
    return result

def main():
    print(solve(20))


if __name__ == "__main__":
    main()
