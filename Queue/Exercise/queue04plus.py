import sys
sys.path.append("..")

from linkedQueue import LinkedQueue

class TwoQueueStack:
    """두 개의 큐를 사용하여 스택의 push()와 pop()을 구현한 클래스"""
    def __init__(self):
        self.__firstQueue = LinkedQueue()
        self.__secondQueue = LinkedQueue()

    def push(self, x):
        self.__firstQueue.enqueue(x)

    def pop(self):
        for _ in range(self.__firstQueue.size()-1):
            self.__secondQueue.enqueue(self.__firstQueue.dequeue())
        
        returnQueue = self.__firstQueue.dequeue()

        for _ in range(self.__secondQueue.size()):
            self.__firstQueue.enqueue(self.__secondQueue.dequeue())

        return returnQueue
            
if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)

    print(st.pop())
    print(st.pop())
    print(st.pop())