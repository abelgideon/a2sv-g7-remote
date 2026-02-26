class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        targetIs = []

        for i, num in enumerate(nums):
            if num == target:
                targetIs.append(i)

        return targetIs