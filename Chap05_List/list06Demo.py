from list06 import *

a = LinkedListBasic()

a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

a.pop(1, 3)     # 2, 3, 4 삭제 (1~3번째 원소)
a.printList()