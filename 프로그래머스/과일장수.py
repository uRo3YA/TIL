def solution(k, m, score):
    score.sort()

    sum = 0
    for packed in range(len(score), m - 1, -m):
        sum += score[packed - m] * m
    return sum
