"""
n
1^2  + 2^2  + 3^2  + .. + n^2
0 --> 0
1 --> 1
2 --> 5
"""

n = int(input())

# best approach
# print(n * (n + 1) * (2 * n + 1) // 6)

i = 1
result = 0

while i <= n:
    result += i ** 2
    i += 1

print(result)
