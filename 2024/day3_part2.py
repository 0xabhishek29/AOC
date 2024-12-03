import sys
from collections import *
from functools import *
from itertools import *
from math import inf, factorial, isqrt, sqrt, gcd, ceil, floor, log2, log, log10, perm, comb
from heapq import *
from bisect import *
import re


def readIntArr():
    return list(map(int, input().split()))


def readArr():
    return input().split()


def solve():    
    res = 0
    ok = 1

    for s in sys.stdin:
        pat = 'mul\(\d{1,3},\d{1,3}\)'
        mulMatches = [[match.start(), match.group()[4:-1].split(',')] for match in re.finditer(pat, s)]

        command = "do\(\)|don't\(\)"
        commandMatches = [[match.start(), match.end()] for match in re.finditer(command, s)]
        j = 0
        
        for start, (num1, num2) in mulMatches:
            while j < len(commandMatches) and commandMatches[j][0] < start:
                ok = (commandMatches[j][1] - commandMatches[j][0]) == 4
                j += 1
            
            if ok:
                if 1 <= len(num1) <= 3 and 1 <= len(num2) <= 3:
                    res += int(num1) * int(num2)
            
    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')