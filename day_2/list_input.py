"""
2 3 5 7 11 100 -90
"""


numbers = input()
numbers = numbers.split()

for index in range(len(numbers)):
    numbers[index] = int(numbers[index])

print(numbers)
