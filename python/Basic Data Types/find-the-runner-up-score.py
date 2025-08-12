if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))

    x = max(arr)

    c = arr.count(x)

    for i in range(c):
        arr.remove(x)

    print(max(arr))
