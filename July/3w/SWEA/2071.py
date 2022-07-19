# 3
# 3 17 1 39 8 41 2 32 99 2
# 22 8 5 123 7 2 63 7 3 46
# 6 63 2 3 58 76 21 33 8 1   


t=int(input())

for i in range(t):
    num_list=list(map(int,input().split()))
    print(f"#{i+1}",round(sum(num_list)/len(num_list)))
