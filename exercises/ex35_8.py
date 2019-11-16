#!/usr/bin/env python3


def solve(N):
    '''Create a list which contains N lists,
    each list contains N numbers from 0->N-1.

    E.g with N = 10:

    matrix = [
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      ...
      ...
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ]

    Then returns a string looks like below

      0********0
      *1******1*
      **2****2**
      ***3**3***
      ****44****
      ****55****
      ***6**6***
      **7****7**
      *8******8*
      9********9
    '''
    result = None
    matrix = []

    for i in range(N):
        row = list(range(N))
        matrix.append(row)
        row[:i] = '*' * (i+1)
        row[i+1:N-i-1] = '*' * (N-i-1)
        row[N-i-1:] = '*' * (i+1)
        row[i] = str(i)
        row[N-i-1] = str(i)

        matrix[i] = ''.join(row)
    result = '\n'.join(matrix)

    return result
def main():
    print(solve(10))


if __name__ == "__main__":
    main()
