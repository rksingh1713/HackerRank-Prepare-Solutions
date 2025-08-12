from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    d[word].append(i)

for i in range(m):
    word = input()
    if word in d:
        print(" ".join(str(x) for x in d[word]))
    else:
        print("-1")
