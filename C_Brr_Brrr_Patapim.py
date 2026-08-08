t = int(input())

for _ in range(t):
    n = int(input())

    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    p = [0] * (2 * n + 1)
    used = [False] * (2 * n + 1)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            idx = i + j
            val = grid[i - 1][j - 1]
            if p[idx] == 0:
                p[idx] = val
                used[val] = True

    missing = []
    for x in range(1, 2 * n + 1):
        if not used[x]:
            missing.append(x)

    for idx in range(2, 2 * n + 1):
        if p[idx] == 0:
            p[idx] = missing.pop()

    ans = p[2:]
    print(missing[0],*ans)