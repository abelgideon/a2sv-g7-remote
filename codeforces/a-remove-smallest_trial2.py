t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    done = 0

    for i in range(0, n-1):
        if abs(a[i] - a[i+1]) > 1:
            print("NO")
            done = 1
            break
    
    if not done:
        print("YES")