import re

for _ in range(int(input())):
    print(re.fullmatch(r"[+-]?\d*\.\d+", input()) is not None)
