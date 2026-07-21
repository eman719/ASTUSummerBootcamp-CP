for _ in range(int(input())):
     n,k=map(int,input().split())
     wishes=[int(x) for x in input().split()]
     courses=[int(x) for x in input().split()]
     my_dict={i:[] for i in range(1,k+2)}
     for idx, val in enumerate(courses,start=1):
         my_dict[val].append(idx)
     ans=[]
     for i in range(k,0,-1):
         for c in my_dict[i]:
             level=i
             while level < k+1:
                 ans.append(c)
                 level+=1
     print(len(ans))
     print(*ans)