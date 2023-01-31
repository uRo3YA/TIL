n = int(input())
k = int(input())

start, end = 0, k
# k번째 수는 k보다 클 수 없음

while start <= end:
    mid = (start+end) // 2
    cnt = 0

    for i in range(1,n+1):
        cnt += min(mid//i, n)  
  
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)