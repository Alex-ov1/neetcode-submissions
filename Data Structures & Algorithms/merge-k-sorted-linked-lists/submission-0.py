# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = ListNode(0)
        curr = l

        test = []
        for i in lists:
            while i:
                test.append(i.val)
                i = i.next
        test.sort()
        
        for i in test:
            curr.next = ListNode(i)
            curr = curr.next

        return l.next