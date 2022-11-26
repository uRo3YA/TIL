from itertools import combinations

# for tc in range(1, 10 + 1):
#     n, m = map(intinput().split())
#     # 10 1238099084
#     pw=str(m)
#     idx=0
# for x in range(m-1):
#     if pw[x]==pw[x+1]:
#         pw.replace(pw[x],"")

#     ans = 0
#     print(f"#{tc}", ans)
n, m = input().split()
pw = str(m)
n = int(n)

for x in range((n) - 1):
    if pw[x] == pw[x + 1]:
        pw = pw.replace(pw[x], "")
        print(pw)
