cham=int(input())
# 동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
datax=[]
datay=[]
for i in range(6):
    d,dis=map(int,input().split())
    if d==1 or d==2:
        datax.append((d,dis))
    elif d==3 or d==4:
        datay.append((d,dis))
datax=sorted(datax, key = lambda x : x[1])
datay=sorted(datay, key = lambda x : x[1])
# print(datax)
# print(datay)
x1=datax[0]
x2=datay[0]
y1=datax[2]
y2=datay[2]

print(((y1[1]*y2[1])-(x1[1]*x2[1]))*cham)
