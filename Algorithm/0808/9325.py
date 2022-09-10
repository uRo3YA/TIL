# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스의 첫 줄엔 자동차의 가격 s가 주어진다. (1 ≤ s ≤ 100 000)
# 둘째 줄엔 해빈이가 구매하려고 하는 서로 다른 옵션의 개수 n이 주어진다. (0 ≤ n ≤ 1 000)
# 뒤이어 n개의 줄이 입력으로 들어온다. 
# 각 줄은 q 와 p로 이루어져 있는데 q는 해빈이가 사려고 하는 특정 옵션의 개수이고 p는 해당 옵션의 가격이다. (1 ≤ q ≤ 100, 1 ≤ p ≤ 10 000)

for tc in range(1,int(input())+1):
    s=int(input())
    n=int(input())
    total=0
    for i in range(n):
        q,p=map(int,input().split())
        total+=q*p
    print(s+total)