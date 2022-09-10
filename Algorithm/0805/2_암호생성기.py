from collections import deque
import sys
#import deque 
sys.stdin = open("_암호생성기.txt")
#ori_list=[9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551]
#ori_list=[10,6,12,8,9,4,1,3]

while True:
    try:
        tc=int(input())
        
        ori_list=list(map(int,input().split()))
        ori_list=deque(ori_list)
    #while ori_list[-1]>=0:
        while True:
            if ori_list[-1]<=0:
                break
            else:
                #5번이 한 사이클
                cnt=0
                for _ in range(5):
                    cnt+=1
                    first=ori_list.popleft()
                    first-=cnt
                    if first<=0:
                        first=0
                        ori_list.append(0)
                        break
                    ori_list.append(first)
        print(f"#{tc}",*ori_list)        
    except EOFError:
        break
