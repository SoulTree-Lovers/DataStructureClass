import sys
sys.path.append("..")

from linkedStack import LinkedStack

class TwoStackQueue:
    """두 개의 스택을 이용하여 만든 큐 클래스"""
    def __init__(self):
        self.__firstStack = LinkedStack()
        self.__secondStack = LinkedStack()
    
    def enqueue(self, x):
        while not self.__firstStack.isEmpty():
            self.__secondStack.push(self.__firstStack.pop())

        self.__firstStack.push(x)

        while not self.__secondStack.isEmpty():
            self.__firstStack.push(self.__secondStack.pop())

    def dequeue(self):
        return self.__firstStack.pop()
    
if __name__ == "__main__":
    queue1 = TwoStackQueue()

    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)

    print(queue1.dequeue())
    print(queue1.dequeue())
    print(queue1.dequeue())