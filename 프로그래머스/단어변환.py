from collections import deque


def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    queue = deque()
    length = len(words)
    word_length = len(begin)

    def can_change(word, change):
        diff = 0
        for i in range(word_length):
            if word[i] != change[i]:
                diff += 1
        if diff == 1:
            return True
        else:
            return False

    def bfs():
        queue.append([begin, 0])

        # 변환할 수 없는 경우
        if target not in words:
            return 0

        while queue:
            word, depth = queue.popleft()

            # words 목록을 순회하며, 변경 가능한 경우에 큐에 추가.
            # 가장 빨리 target이 되는 경우가 최소 변환과정임 (BFS의 특징)
            for change in words:
                if can_change(word, change):
                    if change == target:
                        return depth + 1
                    else:
                        queue.append([change, depth + 1])

    answer = bfs()
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
