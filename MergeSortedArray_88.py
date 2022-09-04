class Solution1:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n:int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
        return nums1


class Solution2:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n:int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        x = 0
        y = 0
        while x < m or y < n:
            if x == m:
                sorted.append(nums2[y])
                y += 1
            elif y == n:
                sorted.append(nums1[x])
                x += 1
            elif nums1[x] < nums2[y]:
                sorted.append(nums1[x])
                x += 1
            else:
                sorted.append(nums2[y])
                y += 1
        nums1[:] = sorted
        return nums1


class Solution3:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n:int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m - 1
        y = n - 1
        tail = m + n -1
        while x >= 0 or y >= 0:
            if x == -1:
                nums1[tail] = nums2[y]
                y -= 1
            elif y == -1:
                nums1[tail] = nums1[x]
                x -= 1
            elif nums1[x] > nums2[y]:
                nums1[tail] = nums1[x]
                x -= 1
            else:
                nums1[tail] = nums2[y]
                y -= 1
            tail -= 1
        return nums1

