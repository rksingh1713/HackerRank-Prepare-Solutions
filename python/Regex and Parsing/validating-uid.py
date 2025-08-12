import re


def is_valid_uid(uid):
    if len(uid) != 10:
        return False

    if not re.match(
        r"(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)(?:([A-Za-z\d])(?!.*\1)){10}$", uid
    ):
        return False

    if not re.match(r"^[A-Za-z0-9]{10}$", uid):
        return False

    return True


for _ in range(int(input())):
    if is_valid_uid(input()):
        print("Valid")
    else:
        print("Invalid")
