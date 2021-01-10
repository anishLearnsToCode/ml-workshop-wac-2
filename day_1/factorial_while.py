"""
N
N! =  1 * 2 * 3 * ... * N
0! = 1! = 1
4! = 1 * 2 * 3 * 4
"""

n = int(input())

result = 1
i = 1

while i <= n:
    result *= i
    i += 1


print(result)
"""
n = 4
result = 1 * 1 * 2 * 3 * 4
i = 5
1 <= 4 ? true
2 <= 4 ? true
3 <= 4 ? true
4 <= 4 ? true
5 <= 4 ? false
24
"""
