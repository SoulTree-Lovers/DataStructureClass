from heap import *

# print('Heap!')
h1 = Heap([1, 11, 9, 2, 3])
h1.buildHeap()
h1.heapPrint()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)

h1.heapPrint()
h1.deleteMax()
h1.heapPrint()


print(h1.printList())

h2 = Heap([4, 12, 3, 5, 10, 7, 2, 15, 9, 8, 1, 6, 11, 13])
h2.buildHeap()

h2.heapPrint()
print(h2.printList())