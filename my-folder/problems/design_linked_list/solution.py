class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if self.size <= index or index < 0:
            return -1

        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
        return currNode.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        currNode = self.head
        tailNode = Node(val, next = None)
        if self.size == 0:
            self.head = tailNode
        else:
            while currNode.next:
                currNode = currNode.next
            currNode.next = tailNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """*arg = (index, val)"""
        if self.size < index:
            return
        currNode = self.head
        
        if index == 0:
            self.addAtHead(val)
        else:
            # 遞歸到指定的index-1的Node
            # 新Node後接index的Node
            # index-1的Node後接新Node
            for _ in range(index - 1):
                currNode = currNode.next

            addNode = Node(val, currNode.next)
            currNode.next = addNode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        currNode = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index - 1):
                currNode = currNode.next
            currNode.next = currNode.next.next

        self.size -= 1