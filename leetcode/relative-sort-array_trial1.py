class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)
        res = []

        for num in arr2:
            for _ in range(freq[num]):
                res.append(num)
        
        arr1.sort()

        arr2Set = set(arr2)
        for num in arr1:
            if num not in arr2Set:
                res.append(num)
        
        return res