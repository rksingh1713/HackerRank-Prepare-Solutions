sizeA = int(input())
setA = set(map(int, input().split()))
sizeB = int(input())
setB = set(map(int, input().split()))

for i in sorted(setA ^ setB):
    print(i)
