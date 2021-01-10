"""
N! = 1 * 2 * 3 * ... * N
0! = 1! = 1
"""

N = int(input())

result = 1

for x in range(1, N + 1):
    result *= x

print(result)
