class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        maxh = max(height)
        while l < r:
            area = min(height[l], height[r])*(r-l)
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            if ans >= maxh*(r-l):
                break

        return ans
