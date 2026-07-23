class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [1]
        for i in range(1, rowIndex+1):
            l.append(1)
            for j in range(i-1, 0, -1):
                l[j] = l[j] + l[j-1]
        return l