import queue
# x=["python","java","ruby","c"]
# print(x)
# print(x.pop())
# print(x)
l=queue.Queue(maxsize=10)
l.put(9)
print(l.get())
l.put(2)
print(l.get())
