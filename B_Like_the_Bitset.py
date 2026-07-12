t = int(input())

for _ in range(t):
    n = int(input())
    lists = []
    for _ in range(n):
        lists.append(list(map(int, input().split())))
        
    counts = {}
    for line in lists:
        first = line[0]
        counts[first] = counts.get(first, 0) + 1
        
    for num, frequency in counts.items():
        if frequency == n - 1:
            leader = num
            
    for line in lists:
        if line[0] != leader:
            print(leader, *line)
            break