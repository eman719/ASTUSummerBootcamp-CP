t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    seen = set()
    count = 0
    
    for j in range(n - 1, -1, -1):
        if a[j] in seen:
            count = j + 1
            break
        seen.add(a[j])
        
    print(count)