from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
S = sorted([S[i] for i in range(len(S))])

for i in combinations_with_replacement(S, k):
    print("".join(i))
