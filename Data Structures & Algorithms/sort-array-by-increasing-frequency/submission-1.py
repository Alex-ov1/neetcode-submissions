class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        l = sorted(freq, key=lambda x: (freq[x], -x))
        z = []
        for i in l:
            z += [i] * freq[i]
        return z