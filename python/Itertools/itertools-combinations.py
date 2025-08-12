from itertools import combinations

S, k = input().split()
k = int(k)
S = sorted([S[i] for i in range(len(S))])

for i in range(k):
    for j in combinations(S, i + 1):
        print("".join(j))
