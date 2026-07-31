t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    first = []
    rest = []

    for x in a:
        if not first or x != first[-1]:
            first.append(x)
        else:
            rest.append(x)

    ans = first + rest
    print(*ans)