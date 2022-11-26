# a = [1, 3, 2, 5, 4, 5, 2, 3]
# a.sort()
# b = {}
# for i in a:
#     if i in b:
#         b[i] += 1
#     else:
#         b[i] = 1
# print(b)
# c = dict(sorted(b.items(), key=lambda x: x[1], reverse=True))
# dic = []
# for key, val in c.items():
#     for d in range(val):
#         dic.append(key)
# print(dic)
# k = 6
# out = []
# for j in range(k):
#     out.append(dic[j])
# print(len(set(out)))
def solution(k, tangerine):
    tangerine.sort()
    b = {}
    for i in tangerine:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    dic = []
    c = dict(sorted(b.items(), key=lambda x: x[1], reverse=True))
    for key, val in c.items():
        for d in range(val):
            dic.append(key)
    out = []
    for j in range(k):
        out.append(dic[j])
    # print(len(set(out)))
    answer = len(set(out))
    return answer


print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 3, 2, 5, 4, 5, 2, 3]))
