setA = set(map(int, input().split()))
n = int(input())
value = 0

for i in range(n):
    if setA.issuperset(set(map(int, input().split()))):
        value += 1

if value == n:
    print("True")
else:
    print("False")
