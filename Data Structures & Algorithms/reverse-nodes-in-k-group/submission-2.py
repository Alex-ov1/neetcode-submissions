# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = ListNode(0)
        curr = l

        test = []
        while head:
            test.append(head.val)
            head = head.next
        
        final = []
        i = 0
        n = len(test) // k
        for _ in range(n):
            final.extend(reversed(test[i:i+k]))
            i += k
        
        final.extend(test[i:])

        for i in final:
            curr.next = ListNode(i)
            curr = curr.next

        return l.next