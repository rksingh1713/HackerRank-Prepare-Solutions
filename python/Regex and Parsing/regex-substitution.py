import re

f = lambda x: "or" if x.group(0) == "||" else "and"

for _ in range(int(input())):
    print(re.sub("(?<= )([|]{2}|[&]{2})(?= )", f, input()))
