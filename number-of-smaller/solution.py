n, m = map(int, input().split())
 
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
 
count = 0
 
for i in range(len(nums2)):
    while count < len(nums1) and nums2[i] > nums1[count]:
        count += 1
    
    print(count, end=" ")