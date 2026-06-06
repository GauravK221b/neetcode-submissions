# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        actual = length - n + 1
        if actual == 1:
            return head.next

        remove = 0
        curr = head
        prev = None
        while curr:
            remove +=1
            if remove == actual:
                prev.next =  curr.next
            prev = curr
            curr = curr.next
        
        return head
            

