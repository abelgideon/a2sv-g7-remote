class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        smallest = float("inf")

        for i in range(1, n*2+1):
            if i % 2 == 0 and i % n == 0:
                smallest = min(smallest, i)
        
        return smallest