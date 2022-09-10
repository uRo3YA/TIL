# 9
# ENTER
# pjshwa
# chansol
# chogahui05
# lms0806
# pichulia
# r4pidstart
# swoon
# tony9402
N = int(input())
enter = str(input()) #ENTER을 입력받고 시작한다.
cnt= 0 #곰곰티콘 사용횟수
dic = {}

for i in range(1,N):
    word = str(input()) #입장한 사람
    if word =="ENTER": #Enter가 입력되면
        for key, value in dic.items():
            if value ==1:  
                cnt+=1 
        dic={} 
        continue
    if word not in dic:
        dic[word] = 1 

for key,value in dic.items():
    if value==1:
        cnt+=1

print(cnt)      