class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        l = []
        freq = {}
        for i in range(len(strs)):
            if strs[i] not in freq:
                s = []
                s.append(strs[i])

                word = [k for k in strs[i]]
                word.sort()
                for j in range(i+1, len(strs)):
                    sbl = list(strs[j])
                    sbl.sort()
                    if word == sbl:
                        s.append(strs[j])

                for i in s:
                    freq[i] = 1
                l.append(s)
        return l    