t=int(input())
for i in range(t):
    num_list=list(map(int,input().split()))
    max1=max(num_list)
   
    print(f'#{i+1}',max1)
