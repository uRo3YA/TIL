n, k = map(int, input().split())
sum_min = k*(k+1)//2
if sum_min > n:
    print(-1)
elif (n-sum_min) % k == 0:
    print(k-1)
else:
    print(k) 