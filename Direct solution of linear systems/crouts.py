import numpy as np
from scipy.linalg import hilbert, norm


A = hilbert(10);

L = np.zeros((len(A), len(A)))
b = np.zeros((len(A), len(A)))


# print(L)

def crouts(A):

    j = len(A)
    helper1(A, j - 1)

    return [L, b]


def helper1(A, j):
    global L
    global b
    i = len(A)
    if j == 0:

        helper2(A, j, i - 1)


    else:
        helper1(A, j - 1)
        helper2(A, j, i - 1)
    return


def helper2(A, j, i):
    global L
    global b
    p = j - 1
    sum = 0

    if i == 0:

        sum = helper3(A, j, i, p)

        if i == j:
            b[i][j] = 1.0

        if i >= j:
            L[i][j] = A[i][j] - sum
        else:
            b[i][j] = (1 / L[i][i]) * (A[i][j] - sum)


    else:
        helper2(A, j, i - 1)
        sum = helper3(A, j, i, p)
        if i == j:
            b[i][j] = 1.0

        if i >= j:
            L[i][j] = A[i][j] - sum
        else:
            b[i][j] = (1 / L[i][i]) * (A[i][j] - sum)

    return


def helper3(A, j, i, p):
    global L
    global b
    summ = 0
    if p == -1:
        summ = 0

    else:
        summ = helper3(A, j, i, p - 1)

        summ += L[i][p] * b[p][j]

    return summ

[L,b]=crouts(A)