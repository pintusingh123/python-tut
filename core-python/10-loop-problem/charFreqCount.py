# single char freequency count in string 
str = "aabbcddeef";
freq = {};
for ch in str:
  freq[ch] = str.count(ch);
  
print(freq)

# find first frequency 
for ch in freq:
    # print(ch, ":", freq[ch])

    if freq[ch] == 1:
        print("first non repeating char is:",ch);
        break

# Step 2: find 2nd non-repeating
count = 0
for ch in str:
    if freq[ch] == 1:
        count += 1
        if count == 2:
            print("Second non-repeating character:", ch)
            break
else:
    print("Not found")
