import re

S, k = input(), input()

if re.search(f"{k}", S):
    for m in re.finditer(f"(?=({k}))", S):
        print(f"({m.start()}, {m.start() + len(k)-1})")
else:
    print("(-1, -1)")
