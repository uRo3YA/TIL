def solution(s):
    a = list(s)  # s의 리스트화
    b = s.lower()  # 문자열 s를 전부 소문자화
    c = list(b)  # 전부 소문자화 한 문자열s를 리스트화
    c[0] = a[0].upper()  # 문자열 첫번째를 대문자화
    for i in range(len(s) - 1):
        if a[i] == " ":
            c[i + 1] = a[i + 1].upper()
    answer = "".join(c)
    # print(answer)
    return answer


print(solution("3people unFollowed me"))
print(solution("for the last week"))
