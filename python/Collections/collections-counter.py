from collections import Counter

shoes = int(input())
sizes = Counter(list(map(int, input().split())))
sum = 0

for i in range(int(input())):
    size, price = list(map(int, input().split()))
    if sizes[size]:
        sum += price
        sizes[size] -= 1

print(sum)
