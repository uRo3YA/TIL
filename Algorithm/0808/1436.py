N = int(input())
m = 666#처음 666인 수
cnt=0
while True:
    if '666' in str(m):
        cnt+=1
    if cnt == N:
        print(m)
        break       
    m+=1