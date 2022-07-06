N = input()
F = int(input())

temp = int(N[:-2] + '00')

while True :
    if temp % F == 0 :
        break
    temp += 1

print(str(temp)[-2:])