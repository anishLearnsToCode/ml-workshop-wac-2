"""
n
1 + 2 + 3 + ... + n
0 --> 0
"""

n = int(input())

# print(n * (n + 1) // 2)


i = 1
result = 0

while i <= n:
    result += i
    i += 1

print(result)
