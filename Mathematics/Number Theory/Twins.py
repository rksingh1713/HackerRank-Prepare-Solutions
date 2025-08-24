#!/bin/python3

import os
import sys
import math

def simple_sieve(limit):
    """Return list of primes up to sqrt(limit) using standard sieve"""
    mark = [True] * (limit + 1)
    mark[0] = mark[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if mark[i]:
            for j in range(i * i, limit + 1, i):
                mark[j] = False
    return [i for i, is_prime in enumerate(mark) if is_prime]

def solve(n, m):
    # Generate primes up to sqrt(m)
    limit = int(math.sqrt(m)) + 1
    base_primes = simple_sieve(limit)

    # Segmented sieve for [n, m]
    size = m - n + 1
    is_prime = [True] * size
    if n == 1:
        is_prime[0] = False

    for p in base_primes:
        start = max(p * p, ((n + p - 1) // p) * p)
        for j in range(start, m + 1, p):
            is_prime[j - n] = False

    # Collect primes in [n, m]
    primes = [i for i in range(n, m + 1) if is_prime[i - n]]

    # Count twin primes
    count = 0
    for i in range(1, len(primes)):
        if primes[i] - primes[i - 1] == 2:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, m = map(int, input().split())
    result = solve(n, m)
    fptr.write(str(result) + '\n')

    fptr.close()
