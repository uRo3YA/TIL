# 3 
# 3 17 1 39
# 8 22 5 10
# 6 53 2 12   
# 첫 번째 수가 시를 나타내고 두 번째 수가 분을 나타낸다.
#  그 다음 같은 형식으로 두 번째 시각이 주어진다

#시는 1 이상 12 이하의 정수이다. 분은 0 이상 59 이하의 정수이다.

for i in range(1,int(input())+1):
    h1,m1,h2,m2=map(int,input().split())
    h3=h1+h2
    m3=m1+m2
    if m3>59:
        h3+=1
        m3%=60
    if h3>12:
        h3%=12
    print(f"#{i}",h3,m3)
