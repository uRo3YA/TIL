num_list=[]
a=int(input())
for i in range(a):
    x=list(map(int,input().split()))
    x.sort(reverse=True)
    num_list.append(x[2])
#print(num_list)
for i in num_list:
    print(i)