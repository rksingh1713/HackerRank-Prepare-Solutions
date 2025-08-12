import re

for _ in range(int(input())):
    print("YES" if re.fullmatch(r"[789][0-9]{9}", input()) else "NO")
