#!/bin/python3

import os
import sys
import math

def solve(n):
    divisors = set()
    # collect all divisors
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    
    divisors.discard(n)  # remove n itself (proper divisors only)
    
    if not divisors:
        return "0"
    
    total = len(divisors)
    count = 0
    
    for d in divisors:
        if d % 2 == 0:  # even check
            root = int(math.isqrt(d))
            if root * root == d:  # perfect square check
                count += 1
    
    if count == 0:
        return "0"
    
    g = math.gcd(count, total)
    return f"{count // g}/{total // g}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = solve(n)
        fptr.write(result + '\n')

    fptr.close()
