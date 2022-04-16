import sys
sys.path.append("..")

from linkedQueue import LinkedQueue

class TwoQueueStack:
    """두 개의 큐를 사용하여 스택의 push()와 pop()을 구현한 클래스"""
    def __init__(self):
        self.__firstQueue = LinkedQueue()
        self.__secondQueue = LinkedQueue()

    def push(self, x):
        if self.__firstQueue.isEmpty():
            self.__firstQueue.enqueue(x)
        else:
            while not self.__firstQueue.isEmpty():
                self.__secondQueue.enqueue(self.__firstQueue.dequeue())
            
            self.__firstQueue.enqueue(x)

            while not self.__secondQueue.isEmpty():
                self.__firstQueue.enqueue(self.__secondQueue.dequeue())
            
    def pop(self):
        return self.__firstQueue.dequeue()
    
if __name__ == "__main__":
    st = TwoQueueStack()
    st.push(1)
    st.push(2)
    st.push(3)

    print(st.pop())
    print(st.pop())
    print(st.pop())