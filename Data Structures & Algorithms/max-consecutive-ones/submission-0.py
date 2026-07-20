class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                count += 1
                maxx = max(maxx, count)
            else:
                count = 0
        return maxx
