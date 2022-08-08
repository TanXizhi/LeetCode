class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = sorted(nums1+nums2)
        if len(x) % 2 == 0:
            return (x[len(x)//2]+x[len(x)//2-1])/2
        else:
            return x[len(x)//2]
