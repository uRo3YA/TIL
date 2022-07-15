import time
N = int(input())
start_time = time.time() # 측정 시작

sum=0
for _ in range(N):
    #a, b = map(int, input().split())
    for _ in range(N):
        sum +=1 

print(sum)
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
