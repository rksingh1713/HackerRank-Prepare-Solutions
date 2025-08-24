#!/bin/python3

import os
import sys

# Extended Euclidean Algorithm to find modular inverse
def modinv(a, m):
    def egcd(a, b):
        if b == 0:
            return (a, 1, 0)
        g, x1, y1 = egcd(b, a % b)
        return (g, y1, x1 - (a // b) * y1)
    
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Inverse does not exist")
    else:
        return x % m

def modpow(a, b, m):
    """Fast modular exponentiation"""
    result = 1
    a %= m
    while b > 0:
        if b & 1:
            result = (result * a) % m
        a = (a * a) % m
        b >>= 1
    return result

def solve(a, b, x):
    if b >= 0:
        return modpow(a, b, x)
    else:
        inv_a = modinv(a, x)
        return modpow(inv_a, -b, x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        a, b, x = map(int, input().split())
        result = solve(a, b, x)
        fptr.write(str(result) + '\n')

    fptr.close()
