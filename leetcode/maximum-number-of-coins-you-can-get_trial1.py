class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0

        L = 0
        R = len(piles) - 1

        while L <= R:
            total += piles[R-1]

            L += 1
            R -= 2
        
        return total