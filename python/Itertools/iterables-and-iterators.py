from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())
sum = 0

combs = list(combinations(letters, k))

for i in combs:
    if "a" in i:
        sum += 1

print(sum / len(combs))
