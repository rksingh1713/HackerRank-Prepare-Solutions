from collections import deque


def check_piling(cubes):
    cubes = deque(cubes)

    left_pile = float("inf")
    right_pile = float("inf")

    while cubes:
        if cubes[0] >= cubes[-1] and cubes[0] <= left_pile:
            left_pile = cubes.popleft()
        elif cubes[0] < cubes[-1] and cubes[-1] <= right_pile:
            right_pile = cubes.pop()
        else:
            return "No"

    return "Yes"


for i in range(int(input())):
    s = int(input())
    cubes = list(map(int, input().split()))
    result = check_piling(cubes)
    print(result)
