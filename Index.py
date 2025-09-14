a=list(map(int,input("enter the number:").split()))
b=int(input("enter the number"))
count=0
for i in a:
    if b==i:
        print("Index", count)
        break
    count=count+1
