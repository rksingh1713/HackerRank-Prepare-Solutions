T = int(input())

for i in range(T):
    elementsA = int(input())
    setA = set(map(int, input().split()))
    elementsB = int(input())
    setB = set(map(int, input().split()))

    if setA.issubset(setB):
        print("True")
    else:
        print("False")
