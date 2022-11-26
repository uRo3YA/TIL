def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
    return answer


print(solution(2, 1, 20))
print(solution(3, 2, 36))
