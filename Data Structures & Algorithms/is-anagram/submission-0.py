class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for i in s:
            if i not in t:
                return False
        
        freqs = {}
        for i in s:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1
        freqt = {}
        for i in t:
            if i not in freqt:
                freqt[i] = 1
            else:
                freqt[i] += 1
        
        for i in freqs:
            if freqs[i] != freqt[i]:
                return False
        
        return True