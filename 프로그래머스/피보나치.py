# F(2) = F(0) + F(1) = 0 + 1 = 1
def fibo(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fibo(n - 2) + fibo(n - 1)


print(fibo(3))
print(fibo(5))
