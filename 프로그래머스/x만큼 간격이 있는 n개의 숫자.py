def solution(x, n):
    answer = []
    for i in range(1,n+1):
        a=(x*i)
        answer.append(a)
    return answer

x=2
n=5
print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))