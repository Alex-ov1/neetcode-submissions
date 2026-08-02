# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = ListNode(0)
        curr = l

        test = []
        while head:
            test.append(head.val)
            head = head.next
        test.pop(len(test)-n)

        for i in test:
            curr.next = ListNode(i)
            curr = curr.next
        
        return l.next