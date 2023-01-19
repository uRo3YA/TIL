a=[]
b=[]
c=[]
for i in range(int(input())):
    n=int(input())
    a=input().split()
    b=input().split()
    c=input().split()
    
    for t in range(n):
        print(c[b.index(a[t])],end=" ")