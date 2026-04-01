# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0

        temp = head
        while temp:
            temp = temp.next
            length += 1
        
        if length == 1 or (length - n) == 0:
            head = head.next
            return head
         
        curr = head
        for _ in range((length - n) - 1):
            curr = curr.next
        
        curr.next = curr.next.next

        return head
