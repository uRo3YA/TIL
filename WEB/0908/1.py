def solution(n):
    answer = 0
    x=3
    while True:
        if x>n:
            answer=0
            break
        if n%x==1:
            answer=x
            break
        else:
            x+=1
    
    return answer

print(solution(10))
print(solution(12))