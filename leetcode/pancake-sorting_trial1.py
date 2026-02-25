class Solution:
    def reverse(self, arr, k):
        L = 0
        R = k-1

        while L < R:
            arr[L], arr[R] = arr[R], arr[L]
            L += 1
            R -= 1
    
    def maxInRange(self, arr, k):
        maxx = float("-inf")
        maxIdx = 0

        for i in range(0, k):
            if arr[i] > maxx:
                maxx = arr[i]
                maxIdx = i
        
        return maxIdx

    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        fixed = len(arr)

        for _ in arr:
            K1 = self.maxInRange(arr, fixed) + 1
            K2 = fixed

            if K1 > 1:
                self.reverse(arr, K1)
                res.append(K1)
            
            if K2 > 1:
                self.reverse(arr, K2)
                res.append(K2)

            fixed -= 1
        
        return res