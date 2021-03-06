class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    def __init__(self, max_size: int):
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = max_size
        self.curr_size = 0
        self.dic = {} # hashmap
     
    def removeNode(self, node):
        """ node의 앞 뒤를 서로 연결 """
        node_after, node_before = node.next, node.prev
        node_before.next, node_after.prev = node_after, node_before
    
    def moveToEnd(self, node):
        prev_node_tail = self.tail.prev
        prev_node_tail.next = node
        node.prev = prev_node_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
            # 해쉬맵에서 못 찾으면 -1
        if key not in self.dic:
            return -1
        node = self.dic[key]
        node_val = node.val
            # 가장 최근에 찾은 노드는 연결 리스트의 맨 뒤(앞에서부터 삭제)로 이동
        self.removeNode(node)
        self.moveToEnd(node)
        return node_val
        
    def put(self, key: int, new_val: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = new_val
            self.removeNode(node)
            self.moveToEnd(node)   
        else:
            if self.curr_size >= self.max_size:
                # 연결리스트 길이가 최대 길이를 넘어갈 경우 앞에서부터 삭제
                old_node = self.head.next
                del self.dic[old_node.key]
                self.removeNode(old_node)
                self.curr_size -=1

            new_node = Node(key, new_val)
            self.dic[key] = new_node
            self.moveToEnd(new_node)
            self.curr_size += 1