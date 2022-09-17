from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_q = deque(truck_weights)
    q = deque([0] * bridge_length)
    t_weight = 0 # 현재 다리의 무게
    
    while q:
        time += 1
        # 나갈 트럭이 있다면 그 무게를 빼준다
        if q[0] != 0: t_weight -= q[0]
        q.popleft()
        if truck_q:
            # 다리의 무게와 대기하는 트럭의 크기가 weight값을 넘지 않으면 더해준다
            if t_weight + truck_q[0] <= weight:
                t_weight += truck_q[0]
                q.append(truck_q.popleft())
            else:
                q.append(0)

    return time
print(solution(2,	10,	[7,4,5,6]))