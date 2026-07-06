n=int(input())
for i in range(n):
    t=int(input())
    s=input()
    operations=0
    for _ in range (len(s)):
        if s[_]!=s[-1]:
            operations+=1
    print(operations)