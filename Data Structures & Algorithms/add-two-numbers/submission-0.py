# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        sum1 = 0
        place1 = 1
        while cur1:
            digit1 = cur1.val
            digit = place1 * digit1
            sum1 += digit
            place1 *= 10
            cur1 = cur1.next
        
        cur2 = l2
        sum2 = 0
        place2 = 1
        while cur2:
            digit = cur2.val
            digit = place2 * digit
            sum2 += digit
            place2 *= 10
            cur2 = cur2.next

        final_sum = sum1 + sum2
        if final_sum == 0:
            return ListNode(0)
        dummy = ListNode()
        curr = dummy
        while final_sum:
            digit = final_sum % 10

            curr.next = ListNode(digit)
            curr = curr.next

            final_sum //= 10

        return dummy.next
        

