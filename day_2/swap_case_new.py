def inverse_case(character: str) -> str:
    return character.upper() if character.islower() else character.lower()


result = ''.join(map(inverse_case, input()))
print(result)
