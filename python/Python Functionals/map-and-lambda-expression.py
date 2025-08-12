cube = lambda x: x**3


def fibonacci(n):
    fib = list()
    x, y = 0, 1
    for i in range(n):
        fib.append(x)
        x, y = y, x + y
    return fib


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
