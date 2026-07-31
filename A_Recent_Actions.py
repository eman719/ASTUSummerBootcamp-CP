t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    ans = [-1] * n
    seen = set()
    idx = n - 1

    for step in range(1, m + 1):
        x = p[step - 1]
        if x not in seen:
            seen.add(x)
            if idx >= 0:
                ans[idx] = step
                idx -= 1

    print(*ans)