"""
1
Dùng numpy để tạo các ma trận sau:
array([[ 0,  1,  2,  3,  4,  5],
       [10, 11, 12, 13, 14, 15],
       [20, 21, 22, 23, 24, 25],
       [30, 31, 32, 33, 34, 35],
       [40, 41, 42, 43, 44, 45],
       [50, 51, 52, 53, 54, 55]])


array(  [[0., 0., 0., 0., 0.],
                 [2., 0., 0., 0., 0.],
                 [0., 3., 0., 0., 0.],
                 [0., 0., 4., 0., 0.],
                 [0., 0., 0., 5., 0.],
                 [0., 0., 0., 0., 6.]])

"""
import numpy as np
def solve():
    # x= np.tile(np.arange(0,60,10),(6,1)).T
    # y = np.array([0,1,2,3,4,5])
    # print(x+y)
    # print()
    result  = []
    A = np.array(range(6))
    B = 10

    for i in range(6):
        result.append(A)
        A = A + B
    print(result)

    zerolst = np.zeros((1,5))
    new_lst_array = np.diag(np.arange(2.,7.))
    concatenate = np.concatenate([zerolst,new_lst_array])
    print('\t'+str(concatenate).replace('\n','\n\t\t'))
solve()