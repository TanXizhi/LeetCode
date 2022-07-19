class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        st = set()
        for i, num in enumerate(nums):
            if i > k:
                st.remove(nums[i-(k+1)])
            if num in st:
                return True
            else:
                st.add(num)
        return False
