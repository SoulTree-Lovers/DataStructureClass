from LinkedListBasicPlus import *

list = LinkedListBasicPlus()
list.append(30)     


list.insert(0, 20)



a = LinkedListBasicPlus()
a.append(4)
a.append(3)
a.append(3)
a.append(2)
a.append(1)



list.extend(a)  

# list = [20, 30, 4, 3, 3, 2, 1]

list.reverse() 


# list = [1, 2, 3, 3, 4, 30, 20]


list.pop(0)


# list = [2, 3, 3, 4, 30, 20]

print("count(3):", list.count(3))
print("get(2):", list.get(2))

list.printList()