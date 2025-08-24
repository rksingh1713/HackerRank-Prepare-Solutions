#!/bin/python3

import sys
import math
import os

def digit_sum(x):
    return sum(int(d) for d in str(x))

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.sqrt(n)) + 1
    for i in range(3, r, 2):
        if n % i == 0:
            return False
    return True

def solve(n):
    # Smith numbers must be composite
    if is_prime(n):
        return 0

    # sum of digits of the number
    s1 = digit_sum(n)

    # prime factorization
    temp = n
    factors = []

    # factor out 2
    while temp % 2 == 0:
        factors.append(2)
        temp //= 2

    # odd factors
    f = 3
    while f * f <= temp:
        while temp % f == 0:
            factors.append(f)
            temp //= f
        f += 2

    if temp > 1:
        factors.append(temp)

    # sum of digits of prime factors
    s2 = sum(digit_sum(fac) for fac in factors)

    return 1 if s1 == s2 else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = solve(n)

    fptr.write(str(result) + '\n')
    fptr.close()
