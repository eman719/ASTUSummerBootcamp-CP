t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue

    q = sorted(p)

    for i in range(n - 1):
        if q[i] == p[i]:
            q[i], q[i + 1] = q[i + 1], q[i]

    if q[-1] == p[-1]:
        q[-1], q[-2] = q[-2], q[-1]

    print(*q)