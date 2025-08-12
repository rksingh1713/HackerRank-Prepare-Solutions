import re

S = input()
p1 = r"[a-z]"
p2 = r"[A-Z]"
p3 = r"[13579]"
p4 = r"[02468]"
print("".join(sorted(re.findall(p1, S))), end="")
print("".join(sorted(re.findall(p2, S))), end="")
print("".join(sorted(re.findall(p3, S))), end="")
print("".join(sorted(re.findall(p4, S))))
