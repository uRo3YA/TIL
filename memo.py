from math import sqrt
import time
start = time.time()  # 시작 시간 저장
n=100000000
m=0
for i in range(n):    
    m+=i
print(m)
 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

start = time.time()  # 시작 시간 저장
k=int(sqrt(n))
z=0
for j in range(k):
    for x in range(k):
        z+=j+k
print(z)
print("time :", time.time() - start)