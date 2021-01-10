"""
N
1 + 2 + 3 + ... + N
"""

n = int(input())
result = 0

for x in range(1, n + 1):
    result += x

print(result)
