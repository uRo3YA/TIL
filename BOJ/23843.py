# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# device_time_list = sorted(map(int, input().split()))

# outlet_list = [0] * m  # 콘센트
# time = 0
# while device_time_list:  # 전자기기를 다 충전할 때까지 반복
#     for i in range(m):
#         if outlet_list[i] == 0:
#             outlet_list[i] = device_time_list.pop()
#             break

#     if 0 not in outlet_list:  # 남는 콘센트가 없다면
#         min_left_time = min(outlet_list)  # 가장 빨리 끝나는 값만큼 시간이 지나야함
#         for i in range(m):
#             outlet_list[i] -= min_left_time

#         time += min_left_time

# # 전자기기를 충전기에 다 꽃았고 나머지가 충전되어 있는 경우
# if outlet_list:
#     time += max(outlet_list)
# print(time)

n, m = map(int, input().split())  # 전자기기 수, 콘센트 수
li = list(map(int, input().split()))

li.sort(reverse=True)

box = li[:m]  # [8, 4]
li = li[m:]  # [4, 1, 1]

for num in li:
    box.sort()
    box[0] += num
    # [4, 8] 4
    # [8, 8] 1
    # [8, 9] 1 # 정렬
print(max(box))
