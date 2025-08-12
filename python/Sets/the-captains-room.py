from collections import Counter

K = int(input())
rooms = Counter(input().split())

for room in rooms:
    if rooms[room] != K:
        print(room)
