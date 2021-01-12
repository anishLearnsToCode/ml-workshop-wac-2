string = input()

result = ''

for character in string:
    if character.islower():
        result = result + character.upper()
    else:
        result = result + character.lower()
    print(result)

print(result)
