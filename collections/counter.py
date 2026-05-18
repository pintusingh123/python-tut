from collections import Counter

data = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = Counter(data)

print(count.most_common(1)) # [('apple', 3)]
print(count.most_common(2)) # [('apple', 3), ('banana', 2)]
print(count.most_common(3)) # [('apple', 3), ('banana', 2), ('orange', 1)]


# case - 2
print("\nCase - 2")
text = "hello world hello python"
word_count = Counter(text.split())
print(word_count)