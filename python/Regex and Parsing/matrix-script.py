#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_script = ""
i = 0

while i < m:
    for x in matrix:
        matrix_script += x[i]
    i += 1

pattern = r"([a-zA-Z0-9])[^(a-zA-Z0-9)]+([a-zA-Z0-9])"
final = re.sub(pattern, r"\1 \2", matrix_script)

print(final)
