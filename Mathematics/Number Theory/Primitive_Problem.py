#!/bin/python3

import sys

def distinct_prime_factors(n):
    factors = set()
    # factor out 2s
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.add(f)
            n //= f
        f += 2
    if n > 1:
        factors.add(n)
    return factors

def euler_phi(n, factors):
    res = n
    for p in factors:
        res = res // p * (p - 1)
    return res

def is_primitive_root(g, p, factors):
    for q in factors:
        if pow(g, (p - 1) // q, p) == 1:
            return False
    return True

if __name__ == "__main__":
    p = int(sys.stdin.readline().strip())

    if p == 2:
        print("1 1")
        sys.exit(0)

    pf = distinct_prime_factors(p - 1)
    total = euler_phi(p - 1, pf)

    gmin = None
    for g in range(2, p):
        if is_primitive_root(g, p, pf):
            gmin = g
            break

    print(str(gmin) + " " + str(total))
