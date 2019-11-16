#!/usr/bin/env python3

import random
def solve(N):
    '''Creates a list which contains N random integers, each >=0, <=9

    To generate 1 random integer, use::

      import random
      random.randrange(0, 10)
    '''
    result = []
    for i in range(N):
        result.append(random.randrange(0,10))
    return result


def main():
    print(solve(10))


if __name__ == "__main__":
    main()
