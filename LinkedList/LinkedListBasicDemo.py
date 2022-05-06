from LinkedListBasic import *

list = LinkedListBasic()
list.append(30)
list.insert(0, 20)

a = LinkedListBasic()
a.append(4)
a.append(3)
a.append(3)
a.append(2)
a.append(1)

list.extend(a)
list.reverse()
list.pop(0)

print("count(3):", list.count(3))
print("get(2):", list.get(6))
print("index(20): ", list.index(20))

print("contains(10): ", list.contains(10))
print("contains(20): ", list.contains(20))

list.printList()
