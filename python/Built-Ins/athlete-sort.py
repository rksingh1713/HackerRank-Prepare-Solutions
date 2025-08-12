#!/bin/python3

import math
import os
import random
import re
import sys


def athleteSort(arr, k):
    sorted_arr = sorted(arr, key=lambda x: x[k])
    for row in sorted_arr:
        print(" ".join(str(y) for y in row))


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr = athleteSort(arr, k)
