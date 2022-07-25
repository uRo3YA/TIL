def fun(x):
    if x<=0:
        return 0
    if x<=3:
        return x
    return fun(x - 2) + fun(x - 3)
a=fun(int(8))
print(a)