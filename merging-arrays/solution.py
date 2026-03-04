n, m = map(int, input().split())
 
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
res = []
 
T = 0
B = 0
 
while T < len(nums1) and B < len(nums2):
    if nums1[T] < nums2[B]:
        res.append(nums1[T])
        T += 1
    else:
        res.append(nums2[B])
        B += 1
 
while T < len(nums1):
    res.append(nums1[T])
    T += 1
 
while B < len(nums2):
    res.append(nums2[B])
    B += 1
 
print(*res)