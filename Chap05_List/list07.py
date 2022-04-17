class BidirectNode:
    """노드 클래스"""
    def __init__(self, x, prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode


class CircularDoublyLinkedList():
    """원형 더블리 링크드 리스트 클래스"""
    def __init__(self):
        """더미 헤드가 있는 버전의 원형 더블리 링크드 리스트"""
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
    def add(self, x):
        

    def printList(self) -> None:
        """리스트를 출력해주는 메소드"""
        for element in self:
            print(element, end = ' ')
        print()

    def getNode(self, i:int) -> BidirectNode:
        """i번째 노드를 가져오는 메소드"""
        curr = self.__head  # 더미 헤드, index: -1
        for _ in range(i+1):
            curr = curr.next
        return curr

    def __str__(self) -> None:
        """리스트를 출력해주는 메소드"""
        for element in self:
            print(element, end = ' ')
        print()
    
    def __iter__(self):     # generating iterator and return
        """이터레이터 메소드"""
        return CircularDoublyLinkedListIterator(self)

class CircularDoublyLinkedListIterator:
    """이터레이터 클래스"""
    def __init__(self, alist):
        self.__head = alist.getNode(-1)         # 더미 헤드
        self.iterPosition = self.__head.next    # 0번 노드

    def __next__(self):
        if self.iterPosition == self.__head:    # 순환 끝
            raise StopIteration
        
        else:                                   # 현재 원소를 리턴하면서 다음 원소로 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item
