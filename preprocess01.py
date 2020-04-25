# Count the words.

from collections import Counter
# counts = Counter(['cat', 'dog', 'cat'])
# print(counts)

with open('data/Treasure_Island.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    words = text.split()

fdist = Counter(words)
obj = fdist.most_common(n=10)
print(obj)


# Word Identification (?)






