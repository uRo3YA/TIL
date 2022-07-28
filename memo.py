sum_list=[]
for i in range(5):
    a,b,c,d=map(int,input().split())   
    sum_list.append(a+b+c+d)
print(sum_list)
tmp=max(sum_list)
print(tmp)
index = sum_list.index(tmp)
print(index)    
print(index+1, max(sum_list))