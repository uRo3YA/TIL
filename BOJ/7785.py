import sys
n=int(input())
in_list={}
for i in range(n):
    name,state= map(str, input().split())
    if state == "enter":
        in_list[name]='enter'
    else:
        del in_list[name]     
result = sorted(in_list.keys(), reverse=True)
for i in result:
    print(i)