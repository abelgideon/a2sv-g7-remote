n, t = map(int, input().split())
books = list(map(int, input().split()))
 
totalSum = 0
L = 0
maxLen = 0
 
for R in range(n):
    totalSum += books[R]
    while totalSum > t and L <= R:
        totalSum -= books[L]
        L += 1
 
    maxLen = max(maxLen, R - L + 1)
 
print(maxLen)