t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    left = 0
    right = n - 1
    mismatches = []
    
    while left < right:
        if s[left] != s[right]:
            mismatches.append(left)
        left += 1
        right -= 1
        
    if not mismatches:
        print("Yes")
    else:
        possible = True
        for i in range(len(mismatches) - 1):
            if mismatches[i + 1] - mismatches[i] > 1:
                possible = False
        if possible:
            print("Yes")
        else:
            print("No")