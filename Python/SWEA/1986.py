
t=int(input())
for i in range(t):
    n=int(input())
    num_list=[]
    for j in range(1,n+1):
        if j %2 ==0:
            num_list.append(-j)        
        else:
            num_list.append(j)        
    print(f'#{i+1}',sum(num_list))