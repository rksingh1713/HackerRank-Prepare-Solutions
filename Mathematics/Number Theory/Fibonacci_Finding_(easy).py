#!/bin/python3

import os
import sys

MOD = 10**9 + 7

def mat_mult(A, B):
    """Multiply 2x2 matrices modulo MOD"""
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(M, power):
    """Fast exponentiation of 2x2 matrix"""
    result = [[1, 0], [0, 1]]  # Identity matrix
    while power > 0:
        if power % 2 == 1:
            result = mat_mult(result, M)
        M = mat_mult(M, M)
        power //= 2
    return result

def solve(a, b, n):
    if n == 0:
        return a % MOD
    if n == 1:
        return b % MOD
    
    # Transformation matrix
    M = [[1, 1], [1, 0]]
    Mn = mat_pow(M, n-1)
    
    # F(n) = Mn[0][0]*b + Mn[0][1]*a
    Fn = (Mn[0][0]*b + Mn[0][1]*a) % MOD
    return Fn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())
    for _ in range(t):
        a, b, n = map(int, input().split())
        result = solve(a, b, n)
        fptr.write(str(result) + '\n')

    fptr.close()
