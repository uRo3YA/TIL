a=int(input())
a_list=list(map(int,input().split()))
battery = 100
prev_ph = -1
prev_con = 0

for i in range(a):
    if a_list[i] != prev_ph:
        battery -=2
        prev_con = 2
    else:
        battery -= prev_con * 2
        prev_con *= 2

    prev_ph = a_list[i]

    if battery <= 0:
        battery = 100
        prev_ph = -1
        prev_con = 0
            
print(100 - battery)
