class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum():
                i = i.lower()
                l.append(i)

        for i in range(len(l)):
            if l[i] != l[-1-i]:
                return False
        return True