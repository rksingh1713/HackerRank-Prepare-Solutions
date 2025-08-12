e = int(input())
Eroll = set(map(int, input().split()))
f = int(input())
Froll = set(map(int, input().split()))

print(len(Eroll | Froll))
