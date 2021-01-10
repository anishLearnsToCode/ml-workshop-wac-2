def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# nPr = n! / (n - r)!
def permutation(n, r):
    return factorial(n) // factorial(n - r)
    # return factorial(4) // factorial(4 - 0)
    # return 24 // factorial(4 - 0)
    # return 24 // factorial(4)
    # return 24 // 24
    # return 1


# nCr = nPr / r!
def combination(n, r):
    return permutation(n, r) // factorial(r)


print(combination(5, 0))
print(combination(5, 1))
print(combination(5, 2))
print(combination(5, 3))
print(combination(5, 4))
print(combination(5, 5))
