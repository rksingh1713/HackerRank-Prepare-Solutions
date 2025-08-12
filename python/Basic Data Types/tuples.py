if __name__ == "__main__":
    n = int(input())

    t = tuple(map(int, input().split()))

    n = int(t.__hash__())

    print(n)
