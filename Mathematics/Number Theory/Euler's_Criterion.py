#!/bin/python3

import os
import sys

def solve(a, m):
    # Special case: if a == 0, X = 0 is a valid solution
    if a == 0:
        return "YES"
    
    val = pow(a, (m - 1) // 2, m)
    if val == 1:
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
