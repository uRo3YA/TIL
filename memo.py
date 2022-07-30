from math import sqrt


n=int(input())
#m=sqrt(n)
m=(int(sqrt(n)))
m_list=[]

## 11 9
while True:
    if n==0:
        break
    if n>=(m**2):
        m_list.append(m) 
        n=n-(m**2) 
    else:
        m-=1
print(len(m_list))
print((m_list))