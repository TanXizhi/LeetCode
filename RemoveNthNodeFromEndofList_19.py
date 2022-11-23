# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#暴力法，先计算长度
class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:   
        def getLength(head: Optional[ListNode]):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        dummy = ListNode(0, head)
        point = dummy 
        length = getLength(head)
        for i in range(1,length-n+1 ):
            point = point.next
        point.next = point.next.next
        return dummy.next


#快慢指针
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:         
        dummy = ListNode(0, head)
        first = head
        second = dummy 
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next 
        second.next = second.next.next
        return dummy.next

#栈
class Solution3:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:         
        dummy = ListNode(0, head)
        point = dummy 
        stack = []
        while point:
            stack.append(point)
            point = point.next
        for i in range(n):
            stack.pop()
        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next