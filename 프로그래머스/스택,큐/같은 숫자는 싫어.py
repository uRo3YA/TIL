def solution(arr):
    answer = []
    for i in arr:
        if len(answer)==0:
            answer.append(i) 
        elif i != answer[-1]:
            answer.append(i)
    return answer
print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))
