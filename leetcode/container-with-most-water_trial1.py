class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxContainer = 0

        while L < R:
            currArea = min(height[L], height[R]) * (R - L)
            maxContainer = max(maxContainer, currArea)

            if height[L] > height[R]:
                R -= 1
            else:
                L += 1
        
        return maxContainer