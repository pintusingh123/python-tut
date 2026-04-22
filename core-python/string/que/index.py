# wirte progranm to count char  in a string 
# one way  
# text = "hello"
# count = {}

# for ch in text:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1

# print(count)


# second way using get methods 
# text = "hello"
# count = {}

# for ch in text:
#       count[ch] = count.get(ch, 0) + 1



# print(count)

# remove duplicate cha in a string 
 
# text = "programming"
# result = ""
# for ch in text:
#   if ch not in result:
#     result = result + ch

# print(result)


# immutibility of string
text = "hello"
# text[0] = "H"  error ayega
text = "H" + text[1:]
print(text)