t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    p1_valid = [False] * n
    sum1 = 0
    for i in range(n - 2):
        sum1 += 1 if a[i] == 1 else -1
        if sum1 >= 0:
            p1_valid[i] = True

    possible = False
    
    has_p1 = False
    sum2 = 0
    
    for j in range(n - 1):
        if p1_valid[j]:
            has_p1 = True
            sum2 = max(0, sum2)  
            
        if has_p1:
            sum2 += -1 if a[j + 1] == 3 else 1
            if sum2 >= 0 and j + 1 < n - 1:
                possible = True
                break

    if possible:
        print("YES")
    else:
        print("NO")