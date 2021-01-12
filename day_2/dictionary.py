"""
dictionary / hash map / hash table

list
index --> value
int --->  anything
[0, n - 1]

{}
key --> value
anything --> anything
unique --> not unique

- mutable
- iterable
"""

words = {'hello': 90, 'i': 550, 'am': 120, 'batman': 13, 'ball': 120}
# print(type(words))

# print(words)
# print(len(words))

# accessing
# print(words['world'])
# print(words.get('world', 'hello world'))

# assigning
print(words)

# remove values from the dict
del words['hello']

# adding a key
words['new key'] = -100

print(words)
