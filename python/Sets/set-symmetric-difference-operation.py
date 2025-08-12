Enews = int(input())
Esubs = set(map(int, input().split()))
Fnews = int(input())
Fsubs = set(map(int, input().split()))

print(len(Esubs.symmetric_difference(Fsubs)))
