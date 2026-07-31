class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            n = len(i)
            res += (str(n)+"#"+i)
        return res

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            n = int(s[i:j])
            word = s[j+1: j+1+n]
            l.append(word)

            i = j+1+n
        return l