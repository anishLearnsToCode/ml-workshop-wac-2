import random

a, b = -100, 100
# r = random.random()
# print(int((b - a) * r + a))

print(random.randint(a, b))

"""
(a, b)
(0, 1) * (b - a)
(0, b - a) + a
(a, b)
"""
