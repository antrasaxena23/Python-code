a=list(map(int,input().split()))
ans=float("inf")
for i in a:
    if(ans<i):
        ans = i
        print(ans)