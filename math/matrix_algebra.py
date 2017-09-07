# Matrix Algebra

import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])
u = np.matrix([[6,2,-3,5]])
v = np.matrix([[3,5,-1,4]])
w = np.matrix([[1],[8],[0],[5]])

# 1. Matrix Dimensions
#  1) A: (2,3)
#  2) B: (2,2)
#  3) C: (3,2)
#  4) D: (2,3)
#  5) u: (1,4)
#  6) w: (4,1)
print(A.shape)
print(B.shape)
print(C.shape)
print(D.shape)
print(u.shape)
print(w.shape)

# 2. Vector Operations
#  1. u+v = [[9,7,-4,9]]
#  2. u-v = [[3,-3,-2,1]]
#  3. 6u = [[36,12,-18,30]]
#  4. u.v = 51
#  5. norm of u = sqrt(74) or ~8.60
print(u+v)
print(u-v)
print(6*u)
print(np.dot(u,v.T))
print(np.linalg.norm(u))

# 3. Matrix Operations
#  1. A+C = not defined
#  2. A-C(T) = [[-4,-7,-3],[3,6,4]]
#  3. C(T)+3D = [[14,3,3],[2,7,9]]
#  4. BA = [[-1,-5,-1],[2,7,4]]
#  5. BA(T) = not defined
print(A-C.T)
print(C.T+3*D)
print(B*A)

# Optional
#  6. BC = not defined
#  7. CB = [[5,-6],[9,-8],[6,-6]]
#  8. B^4 = [[1,-4],[0,1]]
#  9. AA(T) = [[14,28],[28,69]]
#  10. D(T)D = [[10,-4,0],[-4,8,8],[0,8,10]]
print(C*B)
print(B**4)
print(A*A.T)
print(D.T*D)
