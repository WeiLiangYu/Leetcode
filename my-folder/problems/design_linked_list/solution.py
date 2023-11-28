class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size :
            return -1

        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
        return currNode.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val, None)
        else:
            currNode = self.head
            while(currNode.next):
                currNode = currNode.next
            currNode.next = Node(val, None)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.head = Node(val, self.head)
        else:
            currNode = self.head
            for _ in range(index-1):
                currNode = currNode.next
            addNode = Node(val, currNode.next)
            currNode.next = addNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index > self.size-1 or index < 0:
            return

        currNode = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                currNode = currNode.next
            currNode.next = currNode.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)