# 조건1
# 리스트에서 추출한 원소의 양 옆값은 쓸 수 없다
# 조건2
# 맨끝 배열과 맨처음 배열은 연결되어 있다.
# 조건 3
# 추출한 원소의 최대합 구하기
def solution(sticker):
    n=len(sticker)
    if n==1:
        return sticker[0]
    
    d1 = [0] * n
    d2 = [0] * n
    # d1은 맨 앞 뜯는 경우
    d1[0] = sticker[0]
    d1[1] = d1[0]
    for i in range(2, n-1):
        d1[i] = max(d1[i-2]+sticker[i], d1[i-1])
    print("d1:",d1)
    # d2는 맨 앞 뜯지 않는 경우
    for i in range(1, n):
        d2[i] = max(d2[i-2]+sticker[i], d2[i-1])
    print("d2:",d2)
    return max(d1[-2], d2[-1])

solution([14, 6, 5, 11, 3, 9, 2, 10])
solution([1, 3, 2, 5, 4])