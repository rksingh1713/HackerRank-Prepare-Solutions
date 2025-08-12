n, l = int(input()), list(map(int, input().split()))

print(all(i >= 0 for i in l) and any((str(i) == str(i)[::-1]) for i in l))
