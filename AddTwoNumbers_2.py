# Definition for singly-linked list.
# class ListNode;
#     def __init__(self, val=0, next = None):
#         self.val = val
#         self.next = next

class Solution1:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = point = ListNode()
        carry = 0

        while l1 or l2:
            if not l1:
                sum_ = l2.val + carry
                carry, val = divmod(sum_, 10)
                l2 =l2.next
            elif not l2:
                sum_ = l1.val + carry
                carry, val = divmod(sum_, 10)
                l1 =l1.next
            else:
                sum_ = l1.val + l2.val + carry 
                carry, val = divmod(sum_, 10)
                l1 = l1.next
                l2 = l2.next
            point.next = ListNode(val)
            point = point.next
        
        if carry:
            point.next = ListNode(1)
        return head.next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = point = ListNode()
        carry = 0

        while carry or l1 or l2:
            val = carry 
            if l1:
                val = l1.val + val
                l1 = l1.next 
            if l2:
                val = l2.val + val 
                l2 = l2.next
            carry, val = divmod(val, 10)
            point.next = ListNode(val)
            point = point.next
        return head.next
