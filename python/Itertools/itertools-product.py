from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for item in sorted(list(product(A, B))):
    print(item, end=" ")
