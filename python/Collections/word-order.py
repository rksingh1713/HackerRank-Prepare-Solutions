from collections import defaultdict

n = int(input())
words = defaultdict(int)

for i in range(n):
    word = input()
    words[word] += 1

print(len(words))

for word in words:
    print(words[word], end=" ")
