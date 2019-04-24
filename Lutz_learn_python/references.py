L1 = [1, 2, 3]
L2 = L1

L1[0] = 24

print(L1, L2)  # reference on one object

L1 = [2, 3, 4, 5]
L2 = L1[:]

L1[0] = 48

print(L1, L2)

L = [1, 2, 3]

M = L

print(L == M)
print(L is M)

M = [1, 2, 3]

print(L == M)
print(L is M)

import sys
print(sys.getrefcount(1))