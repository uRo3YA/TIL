from collections import deque
import queue
q=[]
a=[]
n=int(input())
for i in range(n):
    q.append(i+1)
dq=deque(q)
for i in range(n-1):
    
    #b=dq[0]
    c=dq.popleft()
    a.append(c)
    b=dq[0]
    dq.append(b)
    #dq.pop()
    dq.popleft()
    #print(dq)   
#for i in range(len(q),0,-1):
#print(dq)
for i in a:
    print(i,end=" ")
print(dq[0])