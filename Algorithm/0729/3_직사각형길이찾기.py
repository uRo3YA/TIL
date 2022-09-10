import sys

sys.stdin = open("_직사각형길이찾기.txt")

for tc in range(1,int(input())+1):
    abc_list=list(map(int,input().split()))
    sq={}
    for i in abc_list:
        if i not in sq:
            sq[i]=1
        else:
            del sq[i]
    for key in sq.keys():
        print(f"#{tc}",key)