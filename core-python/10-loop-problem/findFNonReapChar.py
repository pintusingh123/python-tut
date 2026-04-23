# find first non repeating character in a string
str = "tieeter"
for i in str:
    # print(str.count(i), end=" ")
    if str.count(i) == 1:
        print("first non repeating char is:",i);
        break
    


# charactor freequency in a string
str = "tieeter";
freq = {};
for ch in str:
    # case 1

    freq[ch] = str.count(ch)
print(freq)

    # case 2
    # if ch in freq:
    #     freq[ch] += 1;
    # else:
    #     freq[ch] = 1;

# print(freq)