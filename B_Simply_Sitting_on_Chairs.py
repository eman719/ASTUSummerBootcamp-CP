input_data = open(0).read().split()

if input_data:
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        p = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        pos = {v: i for i, v in enumerate(p)}
        
        matching_passed = [0] * (n + 2)
        current_passed = 0
        for j in range(1, n + 1):
            matching_passed[j] = current_passed
            if p[j-1] <= j:
                current_passed += 1
        matching_passed[n+1] = current_passed
        
        B = [0] * (n + 2)
        for M in range(1, n + 1):
            minus_term = 1 if pos[M] < M - 1 else 0
            plus_term = 1 if p[M-1] > M else 0
            B[M+1] = B[M] - minus_term + plus_term
            
        max_chairs = matching_passed[n+1] + B[n+1]
        
        for M in range(1, n + 1):
            if pos[M] < M - 1:
                chairs_sat = matching_passed[M] + B[M]
                if chairs_sat > max_chairs:
                    max_chairs = chairs_sat
                    
        out.append(str(max_chairs))
        
    print('\n'.join(out))