t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    sorted_s = sorted(s)
    max1 = sorted_s[-1]
    max2 = sorted_s[-2]

    ans = []
    for x in s:
        if x == max1:
            ans.append(x - max2)
        else:
            ans.append(x - max1)

    print(*ans)