t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    found = False

    for j in range(1, n - 1):
        left = -1
        right = -1

        for i in range(j):
            if p[i] < p[j]:
                left = i
                break

        for k in range(j + 1, n):
            if p[k] < p[j]:
                right = k
                break

        if left != -1 and right != -1:
            print("YES")
            print(left + 1, j + 1, right + 1)
            found = True
            break

    if not found:
        print("NO")