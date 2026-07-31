class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        prefix = 1
        for i in range(n):
            l[i] = prefix
            prefix *= nums[i]
        
        sufix = 1
        for i in range(n-1, -1, -1):
            l[i] *= sufix
            sufix *= nums[i]
        
        return l
