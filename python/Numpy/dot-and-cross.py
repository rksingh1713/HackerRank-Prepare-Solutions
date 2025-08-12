import numpy as np

n = int(input())

arrA = np.array([input().split() for _ in range(n)], int)
arrB = np.array([input().split() for _ in range(n)], int)

print(np.dot(arrA, arrB))
