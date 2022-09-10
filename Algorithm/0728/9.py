n,m=map(int,input().split())
n_list=set()
m_list=set()
#nm_list=[]
cnt=0
for i in range(n):
    name=input()
    n_list.add(name)
for i in range(m):
    name=input()
    m_list.add(name)

nm_list=sorted((n_list&m_list))
"""for i in range(n):
    for j in range(m):
        if n_list[i] == m_list[j]:
            cnt+=1
            nm_list.append(n_list[i])"""
#nm_list.sort()
print(len(nm_list))
for i in range(len(nm_list)):
    print(nm_list[i])