n, x = map(int, input().split())
s = []

s = [list(map(float, input().split())) for _ in range(x)]

z = list(zip(*s))

print(*(sum(z[i]) / x for i in range(n)), sep="\n")
