def func(x, cnt):
    if len(x) > 1:
        cnt += 1
        t = 0
        for i in x:
            t += int(i)
        func(str(t), cnt)
    else:
        if int(x) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")


n = input()
cnt = 0
func(n, cnt)
