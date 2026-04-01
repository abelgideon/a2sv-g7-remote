# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        combined = ListNode(0)
        curr = combined

        p1 = list1
        p2 = list2

        while p1 and p2:
            newNode = ListNode()
            if p1.val < p2.val:
                newNode.val = p1.val
                curr.next = newNode
                curr = curr.next
                p1 = p1.next
            else:
                newNode.val = p2.val
                curr.next = newNode
                curr = curr.next
                p2 = p2.next
        
        while p1:
            newNode = ListNode()
            newNode.val = p1.val
            curr.next = newNode
            curr = curr.next
            p1 = p1.next
        
        while p2:
            newNode = ListNode()
            newNode.val = p2.val
            curr.next = newNode
            curr = curr.next
            p2 = p2.next

        
        return combined.next
