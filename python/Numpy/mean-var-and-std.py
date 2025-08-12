import numpy as np

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr), 11))
