n = int(input())
switch = list(map(int,input().split()))
switch = [-1] + [True if switch[i]==1 else False for i in range(n)]
for _ in range(int(input())):
    s,num = map(int,input().split())
    if s == 1:
        for i in range(num,n+1,num):
            switch[i] = not switch[i]
    else:
        switch[num] = not switch[num]
        i,j = num-1,num+1
        while True:
            if i<1 or j>n:
                break
            if switch[i] == switch[j]:
                switch[i] = not switch[i]
                switch[j] = not switch[j]
            else:
                break
            i-=1; j+=1
                
switch = [-1]+list(map(int,switch[1:]))
for i in range(1,n+1):
    print(switch[i], end=" ")
    if i%20 == 0:
        print()