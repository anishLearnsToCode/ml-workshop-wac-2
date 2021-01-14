square = lambda x: x ** 2


# print(type(square))

# print(square(3))
# print(square(4))
# print(square(0))

def lower_case(string: str) -> str:
    return string.lower()


# result = list(map(lambda z: z ** 3, [1, 2, 10, -4, 5]))
# print(result)

# print('--'.join([lower_case(character) for character in 'Hello WOrld']))

def g(x):
    return print(f'hello {x}')


print([g(x) for x in range(-5, 5)])

"""
[None None None ... None]
g(-5)
hello -5
hello -4
hello -3
hello -2
hello -1
hello 0
hello 1
hello 2
hello 3
hello 4
[None None ... None]
"""

# print(print())
