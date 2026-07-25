class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        notin = []
        for i in arr1:
            if i not in arr2:
                notin.append(i)
        notin.sort()

        freq = {}
        for i in arr2:
            freq[i] = 0
        
        z = []
        for i in arr1:
            if i in freq:
                freq[i] += 1
        
        for i in arr2:
            for _ in range(freq[i]):
                z.append(i)
        return z + notin
