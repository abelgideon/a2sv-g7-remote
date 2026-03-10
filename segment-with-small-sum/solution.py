n, s = map(int, input().split())
 
nums = list(map(int, input().split()))
 
runningSum = 0
 
maxLen = 0
 
L = 0
for R in range(n):
    runningSum += nums[R]
 
    while runningSum > s:
        runningSum -= nums[L]
        L += 1
    
    maxLen = max(maxLen, R - L + 1)
 
print(maxLen)