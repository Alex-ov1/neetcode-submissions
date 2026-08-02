# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode(0)
        curr = l

        a = ""
        b = ""
        while l1:
            a += str(l1.val)
            l1 = l1.next
        while l2:
            b += str(l2.val)
            l2 = l2.next
        
        res = str(int(a[::-1]) + int(b[::-1]))
        res = res[::-1]
        
        for i in res:
            curr.next = ListNode(i)
            curr = curr.next

        return l.next