# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## split the ll into half --> we can find the mid value using slow and fast pointer
        ## revrese the second half
        ## merge the both first and second reverse list

        if not head and not head.next:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        ## reverse the second half of the linked list
        prev = None
        curr = second
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        ## prev will the head of the second of the reversed linked list
        ## now merge the first and second half according to the question
        ## head pointing to the first node of the first half and prev pointing to the head 
        ## of second half
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


