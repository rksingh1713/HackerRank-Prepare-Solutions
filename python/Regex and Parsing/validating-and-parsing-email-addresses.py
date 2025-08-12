import re
import email.utils

for _ in range(int(input())):
    parsed_addr = email.utils.parseaddr(input())
    if re.search(r"^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$", parsed_addr[1]):
        print(email.utils.formataddr(parsed_addr))
