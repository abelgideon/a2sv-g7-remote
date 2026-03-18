class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pairs = 0
        window = defaultdict(int)
        goodCount = 0

        L = 0

        for R in range(len(nums)):
            pairs += window[nums[R]]
            window[nums[R]] += 1

            
            while pairs >= k:
                goodCount += (len(nums) - R)

                window[nums[L]] -= 1
                pairs -= window[nums[L]]

                L += 1
        
        return goodCount
                