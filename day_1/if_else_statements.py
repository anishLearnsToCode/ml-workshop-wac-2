"""
if condition_1:
    code
    code
elif condition_2:
    code
elif condition_3:
    code
..
..
..
..
..
else:
    code

elif [optional]
else [optional]
if [compulsory]
"""

number = int(input())
if number == 0:
    print('zero number')
elif number == 1:
    print('puny number')
    print('what a small number')
elif number < 10:
    print('mehhhhhh')
elif number < 100:
    print('large number')
else:
    print('default')

print('i am outside if else block')
