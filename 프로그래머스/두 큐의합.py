def solution(queue1, queue2):
    q = queue1 + queue2
    target = sum(q) // 2

    i, j = 0, len(queue1) - 1
    curr = sum(queue1)
    count = 0

    while i < len(q) and j < len(q):
        if curr == target:
            return count

        elif curr < target and j < len(q) - 1:
            j += 1
            curr += q[j]

        else:
            curr -= q[i]
            i += 1

        count += 1

    return -1


print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
