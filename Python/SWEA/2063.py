t=int(input())
num_list=[]
num_list=list(map(int,input().split()))
#for i in range(t):
    
    #num_list.append(n)
num_list.sort()
#print(num_list)
print(num_list[((t-1)//2)])