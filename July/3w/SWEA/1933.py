#정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
n=int(input())
num_list=[]
for i in range(1,n+1):
    if n % i ==0:
        print (i ,end=" ")