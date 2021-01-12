# iterating over the keys:

words = {'hello': 90, 'i': 550, 'am': 120, 'batman': 13, 'ball': 120}

# for key in words.keys():
#     print(key)

# for key in words:
#     print(key)

# iterate over the values
# for value in words.values():
#     print(value)

# total_words = sum(words.values())
# print(total_words)

# iterate over the items
for key, value in words.items():
    print(key, value)
