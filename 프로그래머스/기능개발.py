progresses=[93, 30, 55]
speeds=[1, 30, 5]

def solution(progresses, speeds):
    answer=[]
    for i in range(len(progresses)):
        p=progresses[i]
        s=speeds[i]
        d=0
        d_cnt=0
        while True:
            if p+(s*d) >= 100:
                break
            d+=1
            d_cnt+=1   
        answer.append(d_cnt)
    return answer

print(solution(progresses, speeds))