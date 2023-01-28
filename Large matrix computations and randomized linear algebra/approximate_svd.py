import numpy as np

A = np.array([[1, 2], [3, 4]])
k = 1
def randomized_svd(A, k):
    p=5;
    m, n = A.shape
    Q = np.random.randn(m, k+p)
    Q, _ = np.linalg.qr(Q)
    B = np.dot(Q.T, A)
    U, Sigma, V = np.linalg.svd(B, full_matrices=False)
    return np.dot(Q, U), Sigma, V


U, S, V = randomized_svd(A, k)
print("U:", U)
print("S:", S)
print("V:", V)