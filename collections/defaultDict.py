# from collections import defaultdict

# d = defaultdict(dict)
# d["a"] = 10 #for dict
#  
# d = defaultdict(list)
# d["b"].append(10) # for list
# print(d)

from collections import defaultdict
count = defaultdict(int)
words = ["apple", "banana", "apple"]

for word in words:
    count[word] += 1

print(count)