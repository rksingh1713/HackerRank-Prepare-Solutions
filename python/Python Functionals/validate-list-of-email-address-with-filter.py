import re


def fun(s):
    reg = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    if re.match(reg, s):
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
