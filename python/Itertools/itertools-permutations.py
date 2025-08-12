from itertools import permutations

S, k = input().split()
k = int(k)
S = [S[i] for i in range(len(S))]


for i in sorted(permutations(S, k)):
    print("".join(i), end="\n")
