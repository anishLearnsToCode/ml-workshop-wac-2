"""
{x^2 | for x in (1, 100)}

[f(i) for i in iterable_object]
"""

# numbers = [x ** 2 for x in range(1, 21)]
# print(numbers)

# letters = [character + '-' for character in 'hello']
# print(letters)

# g = [x for x in range(1, 10)]
# print(g)
# print(type(g))
#
# print(min([1, 2, 3, 4, 100, 0,0, -10, 100]))

# print(max(x for x in range(-5, 5)))

infinity = float('inf')
# print(infinity)
# print(type(infinity))

# g = (x for x in range(-5, 5))
numbers = [-3, -2, 100, 100000, 0.985454, 4354354543]
# max_so_far = -infinity
# for item in numbers:
#     if item > max_so_far:
#         max_so_far = item
#
# print(max_so_far)

# print(sum([1, 2, 3, 4, 5]))
# print(sum(numbers))
# print(sum([x ** 2 for x in range(1, 4)]))

# print(sum(x ** 2 for x in range(1, 4)))

n = int(input())
print(sum(x for x in range(1, n + 1)))
