n,m=map(int,input().split())
lamp=[]
for i in range(n):
    lamp.append(input())

k=int(input())
max_on=0
# print(n,m,lamp,k)
for col in range(n):
    #0 개수
    zero_cnt=0
    for num in lamp[col]:
        if num =="0":
            zero_cnt+=1
    #현재 행에서 똑같은 행의 개수 찾기
    col_lamp_cnt=0
    # print(zero_cnt)
    if zero_cnt<=k and zero_cnt % 2 == k % 2:
        for col2 in range(n):
            if lamp[col]==lamp[col2]:
                col_lamp_cnt+=1
    max_on=max(max_on,col_lamp_cnt)

print(max_on)
