# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the linked list 
        ## go to the nth element 
        ### remove that element 
        ## and finnaly join the element
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        new_head = prev

        previous = None
        current = new_head
        N = 1
        while N < n:
            previous = current
            current = current.next
            N += 1
        
        if previous is None:
            new_head = current.next
        else:
            previous.next = current.next
        # Reverse again to restore original order
        prev = None
        curr = new_head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # return the restored list
        return prev
        
