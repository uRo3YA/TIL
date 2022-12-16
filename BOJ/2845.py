a,b = map(int,input().split())
c = a*b
for i in map(int,input().split()):
    print(i-c, end=" ")