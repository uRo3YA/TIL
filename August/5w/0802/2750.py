n=int(input())
num_list=[]
for i in range(n):
    a=int(input())
    num_list.append(a)
num_list.sort()
for i in range(n):
    print(num_list[i])