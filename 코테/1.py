def solution(v):
    answer = []
    dic1 = {}
    dic2 = {}
    for i, j in v:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1
        if j in dic2:
            dic2[j] += 1
        else:
            dic2[j] = 1
    for key, val in dic1.items():
        if val == 1:
            a = key
    for key, val in dic2.items():
        if val == 1:
            b = key
    answer = [a, b]
    return answer


v = [[1, 4], [3, 4], [3, 10]]
print(solution(v))
