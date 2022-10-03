# 크레인 무게 제한과 박스 무게를 입렫받아 내림차순으로 정렬한다.
n = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
# 시간
time = 0

# 크레인이 옮길 수 있는 무게보다 박스의 무게가 크면
# 크레인으로 박스를 옮길 수 없기때문에 -1을 출력한다.
if crane[0] < box[0]:
    print(-1)
else:
    # 모든 박스를 옮길 때까지 반복
    while box:
        # 각 크레인으로 박스를 옮긴다.
        for i in crane:
            # 박스가 없으면 반복을 멈춤
            if not box:
                break
            # 각 크레인이 옮길 수 있는 무게와 박스의 무게를 내림차순으로 정렬했기 때문에
            # 현재 크레인이 옮길 수 있는 무게보다 마지막 박스의 무게가 크면
            # 현재 남은 크레인으로는 남아있는 박스를 옮길 수 없다.
            elif i < box[-1]:
                break
            else:
                # 박스의 개수만큼 반복한다.
                for j in range(m):
                    # 크레인이 들 수 있는 무게가 박스의 무게보다 크거나 같으면
                    # 박스를 옮겨 팝하고 반복을 멈춤
                    if i >= box[j]:
                        box.pop(j)
                        break

        # 시간 카운트
        time += 1

    print(time)
