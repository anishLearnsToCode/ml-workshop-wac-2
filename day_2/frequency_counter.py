passage = input().split()

frequency = {}

for word in passage:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)
