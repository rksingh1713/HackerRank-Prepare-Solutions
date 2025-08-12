from re import search

regex = search(r"([0-9a-zA-Z])\1+", input())

print(regex.group(1)) if regex else print("-1")
