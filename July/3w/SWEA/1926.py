import pprint
T = int(input())
for i in range(1, T+1):
    s=0
    for x in str(i):
         if x in ['3','6','9']:
            s+=1  
    if s==0:
        print( i, end=' ' )
    else:
        print( '-'*s, end=' ' )