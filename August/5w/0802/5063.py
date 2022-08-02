
#  r은 광고를 하지 않았을 때 수익, 
#  e는 광고를 했을 때의 수익, 
#  c는 광고 비용이다.
#  광고를 해야 하면 "advertise", 
#  하지 않아야 하면 "do not advertise", 
#  광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

# 3
# 0 100 70 advertise
# 100 130 30 does not matter
# -100 -70 40 do not advertise
for i in range(int(input())):
    r,e,c=map(int,input().split())
    if r>e-c:
        print("do not advertise")
    elif r==e-c:
        print("does not matter")
    elif r<e-c:
        print("advertise")