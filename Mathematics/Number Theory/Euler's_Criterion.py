#!/bin/python3

import os
import sys

def solve(a, m):
    # Euler's Criterion: a^((m-1)//2) mod m == 1 => quadratic residue
    if pow(a, (m - 1) // 2, m) == 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        a, m = map(int, input().split())
        result = solve(a, m)
        fptr.write(result + '\n')

    fptr.close()
