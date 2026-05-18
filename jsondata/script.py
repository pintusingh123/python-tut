# convert python-> json
# using json.dumps() method to string
# using json.dump() method to write to a file

import json


data1 = {
  "name":"abc",
  "age":20,
  "is_student":True
}
# json_stringData = json.dumps(data)
# print(type(json_stringData))


# file_path = "D:\\python\\jsondata\\data.json"
# with open(file_path, "w") as f:
#    json.dump(data, f, indent=2)


# conver json -> python
# using json.loads() method to convert string to python data

# json_stringData = '{"name": "abc", "age": 20, "is_student": true}'
# data = json.loads(json_stringData)
# print(data) #dict typed data

# using json.load() method to read from a file and convert to python data
file_path = "D:\\python\\jsondata\\data.json"
with open(file_path, "r") as f:
  data = json.load(f)
  # print( type (data) )  #dict typed data