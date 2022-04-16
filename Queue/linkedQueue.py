from circularDoublyLinkedList import *

class LinkedQueue:
    def __init__(self):
        self.__queue = CircularDoublyLinkedList()
    
    def enqueue(self, x):
        self.__queue.append(x)
    
    def dequeue(self):
        return self.__queue.pop(0)      # pop(0) : 리스트의 첫 번째 원소 삭제 후 리턴
    
    def front(self):
        return self.__queue.get(0)      # get(0) : 리스트의 첫 번째 원소 리턴

    def isEmpty(self) -> bool:
        return self.__queue.isEmpty()
    
    def dequeueAll(self):
        self.__queue.clear()
    
    def size(self):
        return self.__queue.size()

