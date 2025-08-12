import re

m = re.findall(r"(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])", input(), re.IGNORECASE)

print(*m, sep="\n") if m else print(-1)
