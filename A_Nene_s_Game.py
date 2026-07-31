t = int(input())

for _ in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    n_list = list(map(int, input().split()))

    first_elim = a[0]

    ans = []
    for n in n_list:
        ans.append(min(n, first_elim - 1))

    print(*ans)