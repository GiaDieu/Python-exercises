#!/usr/bin/env python3
import random
import string

def solve(N):
    '''Creates a string which contains N random ASCII letters.

    To create 1 letter, use::

      import random
      import string
      random.choice(string.ascii_letters)

    '''
    result = []
    for i in range(N):
        result.append(random.choice(string.ascii_letters))
    return ''.join(result)


def main():
    print(solve(16))


if __name__ == "__main__":
    main()
