# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 刪除頭節點
        while head and head.val == val:
            head = head.next
        # 刪除非頭節點
        currentNode = head
        while currentNode != None and currentNode.next != None:
            if currentNode.next.val == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head