t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n == 1:
        print(1)
        continue
    changes = 0
    same = False
    for i in range(n):
        if s[i] != s[(i + 1) % n]:
            changes += 1
        else:
            same = True
    if same:
        print(changes + 1)
    else:
        print(changes)