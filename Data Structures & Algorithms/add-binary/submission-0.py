class Solution:
    def addBinary(self, a: str, b: str) -> str:
        resa = 0
        resb = 0
        for i in range(len(a)):
            n = len(a)
            if a[n-1-i] == '1':
                resa += 2**i
        for i in range(len(b)):
            n = len(b)
            if b[n-1-i] == '1':
                resb += 2**i
        
        n = resa + resb
        res = ""
        if n == 0:
            return '0'
        while n > 0:
            res += str(n % 2)
            n //= 2
        return res[::-1]