def count_substring(string, sub_string):
    sl = len(string)
    sul = len(sub_string)
    value = 0

    for i in range(sl - sul + 1):
        if string[i : (i + sul)] == sub_string:
            value += 1

    return value


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
