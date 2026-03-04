n = int(input())
nums = list(map(int, input().split()))

hasEven = False
hasOdd = False

for num in nums:
    if hasOdd and hasEven:
        break

    if num % 2 == 0:
        hasEven = True
    else:
        hasOdd = True

if hasEven and hasOdd:
    nums.sort()

print(*nums)