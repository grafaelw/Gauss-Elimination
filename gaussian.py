from Matrix import Matrix as mat
import sys
import unittest

def augment(A,b):
    A.addCol(b)
    return A

def linearSolve(A,b):
    # Reading number of unknowns
    n = len(b)
    if A.numCols()*A.numRows() != n**2:
        sys.exit("Square Matrix A or List b doesn't hold to the same size of arrays !")
    # Making numpy array of n size and initializing to zero for storing solution vector
    x = mat.zeros(n,1)
    # Reading augmented matrix coefficients
    A = augment(A,b)

    # Applying Gauss Elimination
    for i in range(n):
        if A[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        
        for j in range(i+1, n):
            ratio = A[j][i]/A[i][i]
        
            for k in range(n+1):
                A[j][k] = A[j][k] - ratio * A[i][k]

    # Back Substitution
    x[n-1] = A[n-1][n]/A[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = A[i][n]
    
        for j in range(i+1,n):
            x[i] = x[i] - A[i][j]*x[j]
    
        x[i] = x[i]/A[i][i]

    return list(x)
    # # Displaying solution
    # print('\nRequired solution is: ')
    # print(list(x))
    # for i in range(n):
    #      print('X%d = %0.2f' %(i,x[i]), end = '\t')

class GaussianTest(unittest.TestCase):

    def AugmentTest(self):
        A = mat.identity(4)
        b = [2,3,4,5]
        self.assertTrue(augment(A,b) == mat.fromList(list([1,0,0,0,2],[0,1,0,0,3],[0,0,1,0,4],[0,0,0,1,5])))

    def linSolveTest(self):
        # 3-variable Test
        A = mat.fromList([[2,-4,5],[4,-1,0],[-2,2,-3]])
        b = [-33,-5,19]
        self.assertTrue(linearSolve(A,b) == list([-0.5,3,-4]))
        # 4-variable Test
        B = mat.fromList([[1,1,1,1],[-1,2,3,0],[2,3,-4,1],[1,1,2,-1]])
        c = [13,-1,10,1]
        self.assertTrue(linearSolve(B,c) == list([5,-0.25,1.5,6.75]))
    

if __name__=='__main__':
    unittest.main()
