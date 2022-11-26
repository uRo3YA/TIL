def solution(elements):
    result = set()

    elementLen = len(elements)
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]
    elements = elements * 2

    for i in range(elementLen):
        for j in range(elementLen):
            result.add(sum(elements[j : j + i + 1]))
    return len(result)


# [15, 16, 17, 18, 20, 21, 22]
# [8, 14, 15, 16, 17, 18, 20, 21, 22}
# tuple = (10, 22, 19, 2, 9, 3)
# sum_tuple = sum(tuple)
# print(sum_tuple)
