n=int(input())
in_list=[]
ran_list=[]
for i in range(n):
    h,w=map(int,input().split())
    in_list.append((h,w))
#print(in_list)
for i in range(n):
    cnt=0
    for j in range(n):
        if in_list[i][0]<in_list[j][0] and in_list[i][1]<in_list[j][1]:
            cnt+=1
    ran_list.append(cnt+1)
for i in ran_list:
    print(i,end=' ') 
