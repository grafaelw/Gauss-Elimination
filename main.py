import gaussian
from Matrix import Matrix as mat

A = mat.fromList([[2,-4,5],[4,-1,0],[-2,2,-3]])
b = [-33,-5,19]
x=gaussian.linearSolve(A,b)
print(x)