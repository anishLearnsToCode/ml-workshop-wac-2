complex_list = [1, 3.14, 'hello world', print, [1, 2, 3, 4], True, range(1, 10, 3)]

# print(type(complex_list[4]))

# complex_list[3]('hello world', end=' ** ') # --> print('hello world')
# b = print
# c = b

# b('hello')
# print('hello')
# complex_list[3]('hello')
# c('hello')
#

# complex_list[4][0] = 100
# print(complex_list[4])

# print(complex_list)
# complex_list[5] = not True
#
# if complex_list[5]:
#     print('this is true')
# else:
#     print('it is false')
#
#
# for i in complex_list[6]:
#     print(i)


for item in complex_list[4]:
    print(item, end=' ')
