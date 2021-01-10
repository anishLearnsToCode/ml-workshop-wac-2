# continue
# for i in range(10):
#     print(i)
#     if i == 4 or i == 6:
#         continue


"""
i = 9
0
1
2
3
4
5
6
7
8
9
"""

# for i in range(10):
#     if i == 4:
#         break
#     print(i)

# break
for i in range(5):

    for j in range(2):
        if j == 1:
            break
        print(j)

    print(i)

"""
output
i = 4
j = 1
0
0
0
1
0
2
0
3
0
4
"""
