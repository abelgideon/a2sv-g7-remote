# You are given three integers a
# , b
# , and c
# . Determine if one of them is the sum of the other two.

# Input
# The first line contains a single integer t
#  (1≤t≤9261
# ) — the number of test cases.

# The description of each test case consists of three integers a
# , b
# , c
#  (0≤a,b,c≤20
# ).

# Output
# For each test case, output "YES" if one of the numbers is the sum of the other two, and "NO" otherwise.

# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

n = int(input())

for _ in range(n):
    a, b, c = list(map(int, input().split()))

    if a == b + c or b == c + a or c  == a + b:
        print("YES")
    else:
        print("NO")