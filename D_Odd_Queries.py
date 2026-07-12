for _ in range(int(input())):
    n,q=map(int,input().split())
    arr=list(map(int,input().split()))
    prefix_sum=[0]*(n+1)
    for i in range(1,len(prefix_sum)):
        prefix_sum[i]=prefix_sum[i-1]+arr[i-1]
    for _ in range(q):
        total=prefix_sum[-1]
        l,r,k = map(int,input().split())
        unwanted=prefix_sum[r]-prefix_sum[l-1]
        size=r-l+1
        total=total - unwanted +(size*k)
        print("YES") if total %2 !=0 else print("NO")