from collections import namedtuple

person = namedtuple("Person", ["name","age"])
p1=person("alice", 20)
print(p1.name)