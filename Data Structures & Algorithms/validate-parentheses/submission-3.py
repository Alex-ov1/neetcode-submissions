class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        freq = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack or stack[-1] != freq[i]:
                    return False
                stack.pop()
        return not stack