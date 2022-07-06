x,y,w,h =map(int,input().split())

m=min(x,abs(x-w),y,abs(y-h))
print(m)