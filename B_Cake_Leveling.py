t = int(input())
for _ in range(t):

    n = int(input())
    # Read the array of frosting heights
    a = list(map(int, input().split()))
    
    running_sum = 0
    min_avg = None
    results = []
    
    for i in range(n):
        running_sum += a[i]
        current_avg = running_sum // (i + 1)
        
        if min_avg is None:
            min_avg = current_avg
        else:
            min_avg = min(min_avg, current_avg)
            
        results.append(str(min_avg))
        
    print(" ".join(results))

