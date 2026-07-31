t = int(input())

for _ in range(t):
    n = int(input())
    p1 = input().split()
    p2 = input().split()
    p3 = input().split()

    counts = {}
    for w in p1 + p2 + p3:
        counts[w] = counts.get(w, 0) + 1

    ans = [0, 0, 0]
    for i, p in enumerate([p1, p2, p3]):
        for w in p:
            if counts[w] == 1:
                ans[i] += 3
            elif counts[w] == 2:
                ans[i] += 1

    print(*ans)