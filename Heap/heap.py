class Heap:
    """우선 순위 큐 : 힙 클래스"""
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]  # 파라미터로 온 리스트
        else:
            self.__A = []

    # 힙에 원소 삽입하기 (재귀 알고리즘 버전)
    # def insert(self, x):
    #     self.__A.append(x)
    #     self.__percolateUp(len(self.__A)-1)

    #반복문 버전
    def insert(self, x):
        i = len(self.__A) 
        self.__A.append(x)
        parent = (i - 1) // 2
        
        while i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            i = parent
            parent = (i - 1) // 2

    def heapPrint(self):
        a = 0
        b = 1
        while 1:
            for i in range(b):
                if a >= len(self.__A):
                    print("\n===============================")
                    return 0
                print(self.__A[a], end = " ")
                a += 1
            b *= 2
            print()
        
    # 스며오르기
    def __percolateUp(self, i:int):
        parent = (i - 1) // 2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)
    
    # 힙에서 원소 삭제하기
    def deleteMax(self):
        # heap is in self.__A[0...len(self.__A)-1]
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()    # *.pop() : 리스트의 끝 원소 삭제 후 원소 리턴
            self.__percolateDown(0)
            return max
        else:
            return None

    # 스며내리기
    def __percolateDown(self, i:int):
        # Percoate down w/ self.__A[i] as the root
        child = 2 * i + 1   # left child
        right = 2 * i + 2   # right child
        if (child <= len(self.__A)-1):
            if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
                child = right   # index of larger child
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
    
    # 가장 큰 값 리턴하기
    def max(self):
        return self.__A[0]

    # 힙 만들기
    def buildHeap(self):
        for i in range((len(self.__A) - 1) // 2, -1, -1):
            self.__percolateDown(i)
    
    # 힙이 비었는지 확인하기
    def isEmpty(self) -> bool:
        return len(self.__A) == 0

    # 힙 초기화
    def clear(self):
        self.__A = []
    
    # 힙 사이즈
    def size(self) -> int:
        return len(self.__A)
    
    def printList(self):
        return self.__A
        