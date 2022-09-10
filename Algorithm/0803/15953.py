T = int(input())
def code1(n) :
    if n == 1 :
        return 5000000
    elif n > 1 and n < 4 :
        return 3000000
    elif n > 3 and n < 7 :
        return 2000000
    elif n > 6 and n < 11 :
        return 500000
    elif n > 10 and n < 16 :
        return 300000
    elif n > 15 and n < 22 :
        return 100000
    else :
        return 0
    
def code2(n) :
    if n == 1 :
        return 5120000
    elif n > 1 and n < 4 :
        return 2560000
    elif n > 3 and n < 8 :
        return 1280000
    elif n > 7 and n < 16 :
        return 640000
    elif n > 15 and n < 32 :
        return 320000
    else :
        return 0

for i in range(T):
    a, b = map(int, input().split())
    print(code1(a)+code2(b))