class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            minV = float("+inf")
            minI = -1
            for j in range(i, len(arr)):
                if arr[j] < minV:
                    minV = arr[j]
                    minI = j
            
            temp = arr[i]
            arr[i] = arr[minI]
            arr[minI] = temp