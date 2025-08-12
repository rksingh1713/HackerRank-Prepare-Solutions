import re

for _ in range(int(input())):
    matches = re.findall(r"(?<=[:?\s?])(#[0-9a-fA-F]{3,6})(?=[;\s,)])", input())
    for match in matches:
        print(match)
