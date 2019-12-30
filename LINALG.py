from scipy import linalg, array, matmul
from sympy import Matrix

A = array([[1, 0, 0, 0], [-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1]])
AT = A.transpose()
AI = linalg.inv(A)
B = array([[1], [1], [1], [1]])
KI = linalg.inv(matmul(AT, A))
D = array([[2, 1, 1], [-8, -7, -3], [2, -14, 7]])
L, U = linalg.lu(D, True)
L1 = array([[1, 0, 0], [-4, 1, 0], [1, 5, 1]])
U1 = array([[2, 1, 1], [0, -3, 1], [0, 0, 1]])
X = Matrix([[5, 1, 2, 2, 0],
            [3, 3, 2, -1, -12],
            [8, 4, 4, -5, 12],
            [2, 1, 1, 0, -2]])
RX = X.rref()
T = X.T
RT = T.rref()
