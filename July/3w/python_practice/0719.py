# 문제 20. 각 자릿수의 합 구하기
# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
n= 123
x=str(n)
sum1=0
sum2=0
for i in x:
  sum1+=int(i)
print(sum1)

def solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer

print(solution(n))
# 문제 21. 숫자 뒤집기
# 주어진 숫자를 뒤집은 결과를 출력하시오. 
# * 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지
Number=1234
Reverse = 0

while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10

print(Reverse)