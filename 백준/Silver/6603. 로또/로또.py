from itertools import combinations

while True:
    data=list(map(int,input().split()))
    if data[0]==0:
        break
    else:
        # print(f"data:{data[0]}, s:{data[1:]}")
        num=list(combinations(data[1:],6))
        for n in num:
            print(*n) 
    print("")