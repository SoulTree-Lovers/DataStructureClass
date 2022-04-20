from list09 import *

list = LinkedListBasic()
list.append(30)
list.insert(0, 20)

a = LinkedListBasic()
a.append(3)
a.append(3)
a.append(3)
a.append(3)
a.append(2)
a.append(1)
a.append(3)
a.append(3)

list.extend(a)
list.reverse()
list.pop(0)

print("list.lastIndexOf(3): ", list.lastIndexOf(3))

list.printList()
