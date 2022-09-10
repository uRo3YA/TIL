dic={}
cnt=0
for i in range(int(input())):
    cow,now=map(int,input().split())
    if cow not in dic:
        dic[cow]=now
    else:
        if dic[cow]!=now:
            cnt+=1
            dic[cow]=now
print(cnt)