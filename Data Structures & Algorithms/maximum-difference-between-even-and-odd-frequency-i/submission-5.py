class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        l1 = []
        l2 = []
        for i in freq:
            if freq[i] % 2 != 0:
                l1.append(freq[i])
            else:
                l2.append(freq[i])
        
        return max(l1) - min(l2)
