a = int(input())
setA = set(map(int, input().split()))
cmdC = []
cmdN = []

for i in range(int(input())):
    cmdC.append(list(input().split()))
    cmdN.append(set(map(int, input().split())))

    if cmdC[i][0] == "intersection_update":
        setA.intersection_update(cmdN[i])
    if cmdC[i][0] == "update":
        setA.update(cmdN[i])
    if cmdC[i][0] == "symmetric_difference_update":
        setA.symmetric_difference_update(cmdN[i])
    if cmdC[i][0] == "difference_update":
        setA.difference_update(cmdN[i])

print(sum(setA))
