import numpy as np

N, M = map(int, input().split())

array = np.array([input().split() for _ in range(N)], int)

print(array.transpose(), array.flatten(), sep="\n")
