"""
12
(1, 12)
(2, 6)
(3, 4)
(4, 3)
(6, 2)
(12, 1)

16
(1, 16)
(2, 8)
(4, 4)
(8, 2)
(16, 1)

9
(1, 9)
(3, 3)
(9, 1)

sqrt(n)

O(sqrt(n))
"""


def is_prime(number: int) -> bool:
    if number == 1: return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


for i in range(1, 1000):
    if is_prime(i):
        print(i)
