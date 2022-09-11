a=int(input())
a_list=list(map(int,input().split()))
battery = 100
prev_phone = -1
prev_consume = 0

for i in range(a):
    if a_list[i] != prev_phone:
        battery -=2
        prev_consume = 2
    else:
        battery -= prev_consume * 2
        prev_consume *= 2

    prev_phone = a_list[i]

    if battery <= 0:
        battery = 100
        prev_phone = -1
        prev_consume = 0
            
print(100 - battery)
