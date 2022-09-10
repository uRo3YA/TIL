# 3
# level     
# samsung
# eye    


t=int(input())
for i in range(t):
    n=input()
    if n == n[::-1]:
        print(f'#{i+1}',1)
    else:
        print(f'#{i+1}',0)