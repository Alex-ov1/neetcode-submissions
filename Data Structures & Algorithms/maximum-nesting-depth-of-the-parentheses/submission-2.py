class Solution:
    def maxDepth(self, s: str) -> int:
        maxx = 0
        count = 0
        for i in s:
            if i == '(':
                count += 1
                maxx = max(maxx, count)
            elif i == ')':
                count -= 1
        return maxx

