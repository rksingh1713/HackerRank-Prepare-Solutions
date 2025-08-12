from itertools import groupby

s = input().strip()
groups = groupby(s)

result = [(len(list(g)), int(k)) for k, g in groups]
print(*result)
