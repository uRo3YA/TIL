
from collections import defaultdict
n,k=map(int,input().split())
l=list(map(int, input().split()))
s=[0]
ans=0
idx_dic=defaultdict(list)
for i in range(n):
    s.append(s[-1]+l[i])
for j in range(n,0,-1):
    t=s[j]
    if t==k:
        ans+=1
    target=t+k
    # print(target)
    ans+=len(idx_dic[target])
    idx_dic[t].append(j)
# print(idx_dic)
print(ans)