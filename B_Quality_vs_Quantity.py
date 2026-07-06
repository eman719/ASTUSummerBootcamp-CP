t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    blue = a[0]
    red = 0
    i = 1
    j = n - 1
    while i < j:
        blue += a[i]
        red += a[j]
        if red > blue:
            print("YES")
            break
        i += 1
        j -= 1
    else:
        print("NO")
        