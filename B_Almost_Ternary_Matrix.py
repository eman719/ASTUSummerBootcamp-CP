t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    for r in range(n):
        row = []
        for c in range(m):
            if (r % 4 == 0 or r % 4 == 3) == (c % 4 == 0 or c % 4 == 3):
                row.append(1)
            else:
                row.append(0)
        print(*row)