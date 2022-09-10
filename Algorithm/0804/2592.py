dic={}
avg=0
sum=0
for i in range(10):
    a=int(input())
    sum+=a
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
avg=(sum/10)
max_num=max(dic.values())
for key,value in dic.items():
    if max_num==value:
        main_num=key
print(int(avg))
print(main_num)