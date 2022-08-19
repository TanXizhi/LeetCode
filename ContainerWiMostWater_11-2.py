class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                w = j-i
                h = min(height[i], height[j])
                area = h*w
                if area >= ans:
                    ans = area

        return ans
