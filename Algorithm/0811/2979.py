# 트럭을 한 대 주차할 때는 1분에 한 대당 A원을 내야 한다. 
# 두 대를 주차할 때는 1분에 한 대당 B원, 
# 세 대를 주차할 때는 1분에 한 대당 C원을 내야 한다.
# 다음 세 개 줄에는 두 정수가 주어진다. 
# 이 정수는 상근이가 가지고 있는 트럭이 주차장에 도착한 시간과 주차장에서 떠난 시간이다. 
# 도착한 시간은 항상 떠난 시간보다 앞선다. 입력으로 주어지는 시간은 1과 100사이 이다.
a, b, c = map(int, input().split())
arr = [0]*100; answer=0
for _ in range(3):
    begin, end = map(int, input().split())
    for i in range(begin, end): arr[i] += 1
for j in arr:
    answer += {0:0, 1:a, 2:b*2, 3:c*3}[j]
print(answer)
