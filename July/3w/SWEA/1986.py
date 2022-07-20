# N이 5일 경우,
# 1 – 2 + 3 – 4 + 5 = 3
# N이 6일 경우,
# 1 – 2 + 3 – 4 + 5 – 6 = -3
# [제약사항]
# N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.
# [출력]
# 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.

t=int(input())
for i in range(t):
    n=int(input())
    num_list=[]
    for j in range(1,n+1):
        if j %2 ==0:
            num_list.append(-j)        
        else:
            num_list.append(j)        
    print(f'#{i+1}',sum(num_list))