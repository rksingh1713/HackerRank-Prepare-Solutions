n, m = map(int, input().split())
array = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))
h = 0

for i in array:
    if i in setA:
        h += 1
    if i in setB:
        h -= 1

print(h)
