from pprint import pprint


def solution(rows, columns, queries):
    answer = []
    mat = [[row * columns + col + 1 for col in range(columns)] for row in range(rows)]

    for t, l, b, r in queries:
        top, left, bottom, right = t - 1, l - 1, b - 1, r - 1
        tmp = mat[top][left]
        minimum = tmp

        for y in range(top, bottom):
            value = mat[y + 1][left]
            mat[y][left] = value
            minimum = min(minimum, value)

        for x in range(left, right):
            value = mat[bottom][x + 1]
            mat[bottom][x] = value
            minimum = min(minimum, value)

        for y in range(bottom, top, -1):
            value = mat[y - 1][right]
            mat[y][right] = value
            minimum = min(minimum, value)

        for x in range(right, left, -1):
            value = mat[top][x - 1]
            mat[top][x] = value
            minimum = min(minimum, value)

        mat[top][left + 1] = tmp
        answer.append(minimum)
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# (solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
