def prime(x):
    if x ==1:            #1은 모든 수의 약수이기 때문에 pass
        return False
    for i in range(2,int(x**0.5)+1):  #제곱근이 있는 수 중에
        if x%i==0:					#약수가 있으면 false	
            return False
    return True						#이외에는 소수

while True:
    n=int(input())
    count=0
    if n == 0 :						#0 입력하면 아웃되는 게 조건
            break
    for i in range(n,2*n+1):		#n과 2n+1사이에서
        if prime(i):					#sosu함수안에 있는 게 있다면
            count+=1					#카운트를 세라
    print(count)		#개수를 출력하는 조건에 맞춰 카운트를 출력