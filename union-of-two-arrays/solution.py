class Solution:    
    def findUnion(self, a, b):
        # code here
        union = set()
        
        for num in a:
            union.add(num)
        
        for num in b:
            union.add(num)
            
        return union