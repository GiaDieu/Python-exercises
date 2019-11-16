#!/usr/bin/env python3

data = (
    [1, 5, 2, 3, 4],
    [4, 5, 0, 4]
)


# def solve(list1, list2):
#     '''Find common elements of two given lists.

#     Returns a list contains those elements.
#     Require: use only lists, and loop.
#     '''
#     result = []
#     for num in list2:
#         if num in list1:
#             result.append(num)
#     return result


# def main():
#     L1, L2 = data
#     print(solve(L1, L2))


# if __name__ == "__main__":
#     main()

def solve(list1, list2):
    '''Find common elements of two given lists.

    Returns a list contains those elements.
    Require: use only lists, and loop.
    '''
    result = []
    for i in list2:
        if i in list1:
            result.append(i)
    return result

def main():
    L1, L2 = data
    print(solve(L1, L2))


if __name__ == "__main__":
    main()