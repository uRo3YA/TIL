t=int(input())
for i in range(t):
    n=int(input())
    data=[]
    for j in range(n):
        paper,interview=map(int,input().split())
        data.append((paper,interview))
    data=sorted(data, key = lambda x : x[0])
    hired = 1
    man = data[0][1]
    for x in range(1,n) :
        if data[x][1] < man :
            man = data[x][1]
            hired += 1
    print(hired)
    # 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
    # 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.