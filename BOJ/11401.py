import math

n, m = map(int, input().split())
k = (math.factorial(n)) / (math.factorial(m) * ((math.factorial(n - m))))
print(int(k % 1000000007))
