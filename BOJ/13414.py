import sys

input = sys.stdin.readline
k, l = map(int, input().split())
num_list = {}
# 순서를 키로 정할 수도 있지만 값으로도 정할 수 있다.
# 추월 문제와 반대로 생각하기
for i in range(l):
    # int 를 쓰면 01234567 순서가 꼬임
    # 그런데 그냥 받으면 \n을 그대로 읽음
    num = input().rstrip()
    num_list[num] = i

sort_numlist = sorted(num_list.items(), key=lambda x: x[1])
# print("num_list:")
# print("sort_numlist:"sort_numlist)
cnt = 0
for j in sort_numlist:
    # 인덱스 에러
    # 중복이 엄청나게 많다면 k보다
    # sort_numlist가 짧을 수도 있음
    cnt += 1
    if cnt > k:
        break
    print(j[0])
