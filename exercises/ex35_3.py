#!/usr/bin/env python3


def solve(N):
    '''Creates a list which contains N first even integers. ``[2, 4 ...]``
    '''
    result = []
    for i in range(N):
        result.append((i+1)*2)
    return result


def main():
    print(solve(6))


if __name__ == "__main__":
    main()
