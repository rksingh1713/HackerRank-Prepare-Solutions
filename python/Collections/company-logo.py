#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == "__main__":
    [print(*a) for a in Counter(sorted(input())).most_common(3)]
