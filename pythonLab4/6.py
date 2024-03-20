text = 'one two three One two'
words = text.lower().split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
sorted_words = sorted(word_counts, key=lambda w: (-word_counts[w], w))
print(word_counts)

for word in sorted_words:
    print(word)