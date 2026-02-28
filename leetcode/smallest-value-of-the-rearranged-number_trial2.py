class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
            
        isNeg = False

        if num < 0:
            isNeg = True
            num = -num

        strNum = list(str(num))

        if isNeg:
            strNum.sort(reverse=True)
        else:
            strNum.sort() 

        R = 0
        L = 0
        while strNum[R] == "0":
            R += 1

        strNum[L], strNum[R] = strNum[R], strNum[L]

        num = int("".join(strNum))

        if isNeg:
            return -num
        
        return num