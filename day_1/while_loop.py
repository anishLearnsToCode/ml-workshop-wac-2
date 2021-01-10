"""
while condition:
    code
    code

condition (true) --> code --> condition (true) --> code --> condition (false) --> loop ends
(condition --> code) --> condition becomes false
"""

# infinite loop
# while True:
#     print('hello')

i = 0
while i < 5:
    print(i)
    i = i + 2

print(i)
print('i am outside loop')

"""
i = 
0
2
4
6
i am outside loop
"""
