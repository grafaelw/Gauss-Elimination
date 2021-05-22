from Matrix import Matrix as mat
import sys
import unittest


def linearSolve(A, b):
    # Reading number of unknowns
    n = len(b)
    if A.numCols() * A.numRows() != n ** 2:
        sys.exit("Square Matrix A or List b doesn't hold to the same size of arrays !")
    # Making array of n size and initializing to zero for storing solution vector
    x = mat(n)
    # Reading augmented matrix coefficients
    A.addCol(b)

    # Applying Gauss Elimination
    for i in range(n):
        # Pivoting Technique
        for m in range(i, n):
            if A[i][i] == 0.0:
                A.swapRows(i, m)
            else:
                pass

        for j in range(i + 1, n):
            q = A[j][i] / A[i][i]

            for k in range(n + 1):
                A[j][k] -= q * A[i][k]

    # Back Substitution
    x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

    for i in range(n - 1, -1, -1):
        x[i] = A[i][n]

        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

        x[i] /= A[i][i]

    return list(x)
    # # Displaying solution
    # print('\nRequired solution is: ')
    # print(list(x))
    # for i in range(n):
    #      print('X%d = %0.2f' %(i,x[i]), end = '\t')


class GaussianTest(unittest.TestCase):

    def testPivot(self):
        '''Testing the pivoting technique'''
        A = mat.fromList([[0, 1, 0], [1, 1, 2], [1, 2, 1]])
        b = [-1, 2, 1]
        self.assertTrue(linearSolve(A, b) == list([3, -1, 0]))

    def test4var(self):
        A = mat.fromList([[1, 1, 1, 1], [-1, 2, 3, 0], [2, 3, -4, 1], [1, 1, 2, -1]])
        b = [13, -1, 10, 1]
        self.assertTrue(linearSolve(A, b) == list([5, -0.25, 1.5, 6.75]))


if __name__ == '__main__':
    unittest.main()

