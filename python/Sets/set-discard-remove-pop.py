import pdb

m = int(input())
lst = [int(j) for j in input().strip().split()]
lst.reverse()
st = set(lst)
n = int(input())
for i in range(n):
    command = input().strip().split()

    if len(command) == 1:
        methodToCall = getattr(st, command[0])
        methodToCall()

    else:
        commd, *args = [command[0], int(command[1])]
        getattr(st, commd)(*args)

print(sum(st))
