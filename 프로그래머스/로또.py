def solution(lottos, win_nums):
    bestResult = 7
    worstResult = 7
    for i in lottos:
        if (i not in win_nums) and (i == 0):
            bestResult = bestResult - 1
        elif (i != 0) and (i in win_nums):
            bestResult = bestResult - 1
            worstResult = worstResult - 1
    if bestResult > 6:
        bestResult = 6
    if worstResult > 6:
        worstResult = 6

    answer = [bestResult, worstResult]
    return answer


# 1	6개 번호가 모두 일치
# 2	5개 번호가 일치
# 3	4개 번호가 일치
# 4	3개 번호가 일치
# 5	2개 번호가 일치
# 6(낙첨)	그 외

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
