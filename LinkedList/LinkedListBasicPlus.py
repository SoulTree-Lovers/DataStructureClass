class ListNode:
    """연결 리스트의 노드 클래스"""
    def __init__(self, newItem, nextNode : 'ListNode'):
        self.item = newItem
        self.next = nextNode

# Basic 버전에서 __init__(), insert(), append(), pop(), clear(), reverse(), __getNode(), printList() 수정
class LinkedListBasicPlus:
    """헤드가 비어 있는 연결 리스트 클래스"""
    def __init__(self):
        self.__head = None
        self.__numItems = 0

    # 연결 리스트에 원소 삽입하기 
    def insert(self, i:int, newItem):
        if self.__head is None:
            self.__head = ListNode(newItem, None)
            self.__numItems += 1
            
        elif 0 < i <= self.__numItems:
            prev = self.__getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        
        elif i == 0:
            newNode_next = self.__head
            newNode = ListNode(newItem, newNode_next)     
            self.__head = newNode
            self.__numItems += 1

        else:
            print("index", i, ": out of bound in insert()") # 필요 시 에러 처리
    
    # 연결 리스트에 원소 추가하기   
    def append(self, newItem):
        if self.isEmpty():
            self.__head = ListNode(newItem, None)
            self.__numItems += 1
    
        else:
            prev = self.__getNode(self.__numItems - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
            
    # 연결 리스트의 원소 삭제하기 
    def pop(self, i:int): # i번 노드 삭제, 고정 파라미터
        if (i == 0):
            self.__head = self.__getNode(1)
        elif (0 < i <= self.__numItems - 1):
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            return None
      
    # 연결 리스트의 원소 x 삭제하기 (더미 헤드를 두는 대표 버전)
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            prev.next = curr.next
            self.__numItems -= 1
            return x
        else:
            return None
  
    # 연결 리스트의 i번 원소 알려주기
    def get(self, i:int):
        if self.isEmpty():
            return None
        if (0 <= i < self.__numItems):
            return self.__getNode(i).item
        else:
            return None
  
    # x가 연결 리스트의 몇 번째 원소인지 알려주기
    def index(self, x) -> int:
        curr = self.__head.next   # 0번 노드 : 더미 헤드 다음 노드
        for index in range(self.__numItems):
            if curr.item == x:
                return index
            else:
                curr = curr.next
                return -2 # 안 쓰는 인덱스
  
    # 기타 작업들
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems
    
    def clear(self):
        self.__head = ListNode(None, None)
        self.__numItems = 0
  
    def count(self, x) -> int:
        cnt = 0
        if self.__head == None:
            return 0

        else:
            curr = self.__head.next # 0번 노드
            while curr != None:
                if curr.item == x:
                    cnt += 1
                curr = curr.next
            return cnt
  
    def extend(self, a): # a와 self는 같은 타입의 리스트
        for index in range(a.size()):
            self.append(a.get(index))
    
    def copy(self):
        a = LinkedListBasicPlus()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    
    def reverse(self):
        # reversed_list라는 이름의 새로운 리스트를 생성하여 원래 리스트의 값을 거꾸로 삽입한다.
        reversed_list = LinkedListBasicPlus()
        for index in range(self.size()):
            reversed_list.insert(0, self.get(index))
        
        # 원래의 리스트를 초기화한다.
        self.clear()

        # 원래 리스트에 reverser_list의 값을 넣어준다.
        for index in range(reversed_list.size()):
            self.append(reversed_list.get(index))
      
    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a[index])
      
    def __findNode(self, x) -> (ListNode, ListNode):
        prev = self.__head  # 더미 헤드
        curr = prev.next    # 0번 노드
        while curr != None:
            if curr.item == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
            return (None, None)
  
    # 연결 리스트의 i번 노드 알려주기
    def __getNode(self, i:int):
        curr = self.__head
        for index in range(i):       
            curr = curr.next
        return curr

    def printList(self):
        curr = self.__head 
        while curr != None:
            print(curr.item, end = ' ')
            curr = curr.next
        print()