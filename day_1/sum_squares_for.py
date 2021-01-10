"""
N
1^2 + 2^2 + ... + N^2
"""

n = int(input())

result = 0

for i in range(1, n + 1):
    result += i ** 2

print(result)
