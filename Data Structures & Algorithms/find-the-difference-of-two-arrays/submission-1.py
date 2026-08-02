class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen1 = set()
        seen2 = set()

        l1 = []
        l2 = []
        l = []
        for i in nums1:
            if i not in nums2 and i not in seen1:
                l1.append(i)
                seen1.add(i)

        for i in nums2:
            if i not in nums1 and i not in seen2:
                l2.append(i)
                seen2.add(i)
                
        l.append(l1)
        l.append(l2)
        return l