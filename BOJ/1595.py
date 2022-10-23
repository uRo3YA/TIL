from collections import deque, defaultdict


def bfs(i, cost):
    max_node, max_cost = 0, 0
    chk = [0] * (len(road) + 1)
    chk[i] = 1
    queue = deque([[i, cost]])
    while queue:
        u, curr_cost = queue.popleft()
        print(u, curr_cost)
        for v, next_cost in road[u]:
            if not chk[v]:
                chk[v] = 1
                new_cost = curr_cost + next_cost
                if max_cost < new_cost:
                    max_node, max_cost = v, new_cost
                queue.append([v, new_cost])
    # print([max_node, max_cost])
    return [max_node, max_cost]


road = defaultdict(list)
while True:
    try:
        a, b, c = map(int, input().split())
        road[a].append([b, c])
        road[b].append([a, c])
    except:
        break
# 입력중에 유효하지 않은 유형이 있음
print("-------")
print(bfs(bfs(1, 0)[0], 0)[1] if road else 0)
