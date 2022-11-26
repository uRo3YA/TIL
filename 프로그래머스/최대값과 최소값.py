def solution(s):
    arr = list(map(int, s.split()))
    # print(arr)
    min_arr = min(arr)
    max_arr = max(arr)
    answer = str(min_arr) + " " + str(max_arr)
    return answer


print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
