i = 0
while i < 4:
    j = 0
    while j < 2:
        print(i + j, end=' ')
        j = j + 1
    print()
    i = i + 1

print(i + j)

"""
output
i = 1
j = 2
0 1
1 2
2 3
3 4
6
"""
