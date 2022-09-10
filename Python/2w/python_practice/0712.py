#
# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
#01
#n=int(input())
n=6
if n%3 == 0 and n%2==0:
    print("참")
else:
    print("거짓")
#02
#문자열 word의 길이를 출력하는 코드를 1) while문 2) for문(문자열 그대로) 3) for문(index)으로 각각 작성하시오.
word="happy"
l_02_1 = 0
for i in word:
	l_02_1+=1
print(l_02_1)

#03
#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
num03 = 10
i_3=0
sum_03=0
while True:
    if i_3>10:
        print(sum_03)
        break
    sum_03+=i_3
    i_3+=1
sum_03_1=0
for i_3_1 in range(num03+1):
    sum_03_1+=i_3_1
print(sum_03_1)

#04
#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
n_04=5
p_04=1
i_04=0
p_04_1=1
while True:
    i_04+=1
    p_04*=i_04
    if n_04 == i_04:
        print(p_04)
        break
for i_04_1 in range(1,n_04+1):
    p_04_1*=i_04_1 
print(p_04_1)   
#05 
#1부터 n까지의 평균을 구하는 코드를 작성하시오.
num_05 = [3, 10, 20]
cnt_05=0
sum_05=0
for i in num_05:
    sum_05+=i
    cnt_05+=1
print(float(sum_05/cnt_05))

#06
#주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
num_06 = [0, 20, 100, 50, -60, 50, 100]

max_num_06=num_06[0]
for i_06 in num_06:
    if i_06>=max_num_06:
        max_num_06=i_06
print(max_num_06)

#07
#주어진 리스트 numbers에서 최솟값을 구하여 출력하시오.
num_07 = [0, 20, 100, 50, -60, 50, 100]

min_num_07=num_07[0]
for i_07 in num_07:
    if i_07<=min_num_07:
        min_num_07=i_07
print(min_num_07)

#08
#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.
num_08 = [0, 20, 100, 40]
max_number_08 = num_08[0]
second_number_08 = num_08[0]
# 1. 전체 숫자를 반복
for n in num_08:
    # 만약, n이 최대보다 크다면
    if max_number_08 < n:
        # 최댓값이었던 것이 두번째로 큰 수
        second_number_08 = max_number_08
        max_number_08 = n
    # elif second_number < n < max_number:
    elif second_number_08 < n and n < max_number_08:
        second_number_08 = n
print(second_number_08)
