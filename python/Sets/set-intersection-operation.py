Enews = int(input())
Eroll = set(map(int, input().split()))
Fnews = int(input())
Froll = set(map(int, input().split()))

print(len(Eroll.intersection(Froll)))
