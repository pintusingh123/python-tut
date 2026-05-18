# fast and flexiball list-like container with fast appends 
from collections import deque

dq = deque([1,2,3,4,5])

dq.append(10)
dq.appendleft(0)
dq.pop() #end se remove krta hai
dq.popleft() # left se remove karta hai
print(dq)