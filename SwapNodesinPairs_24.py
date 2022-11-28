# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 迭代
class Solution1:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy 
        while cur.next and cur.next.next:
            p1 = cur.next
            p2 = cur.next.next
            cur.next = p2
            p1.next = p2.next
            p2.next = p1
            cur = p1
        return dummy.next


# 递归
class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head 
        
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp