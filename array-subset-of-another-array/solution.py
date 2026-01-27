#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        aCounter = Counter(a)
        
        for num in b:
            if aCounter[num]:
                aCounter[num] -= 1
            else:
                return False
        
        return True