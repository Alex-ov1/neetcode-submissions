# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        l = []
        n = 1
        q = deque([root])
        while q:
            s = []
            for _ in range(len(q)):
                node = q.popleft()
                s.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if n % 2 != 0:
                l.append(s)
            else:
                l.append(s[::-1])
            n += 1
        return l