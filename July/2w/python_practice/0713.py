"""
예제 01
숫자 n을 받아 세제곱 결과를 반환하는 함수 cube를 정의하시오. 
cube 함수를 호출하여 12의 세제곱 결과를 출력하시오.

출력
1728
"""
def cube(x):
    return x**3
x=int(12)
print(cube(x))

"""
예제 02
가로와 세로의 길이를 각각 a, b로 받아 사각형 넓이와 둘레를 함께 반환하는 함수 rectangle을 정의하시오. 
사각형이 가로가 20, 세로가 30일 때의 결과를 출력하시오.

* 사각형 넓이 : 가로 * 세로 
* 사각형 둘레 : (가로 + 세로) * 2

출력
(600, 100)
"""
def rectangle(a,b):
    n=a*b
    l=(a+b)*2
    return n,l
a,b=20,30
print(rectangle(a,b))

"""
문제 09
주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.
입력
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
출력
4
"""

students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
cnt=students.count("이영희")
print(cnt)

"""
문제 10
2단부터 9단까지 반복하여 구구단을 출력하세요.
* 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.

출력
2단
2 X 1 = 2 
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
3단
3 X 1 = 3 
3 X 2 = 6
"""
n=9
for i in range(2,n+1):
    print(f"{i}단")
    for j in range(1,10):
        print(f"{i}X{j}={i*j}")
"""
문제 11
주어진 리스트의 요소 중에서 5의 개수를 출력하시오.
입력
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
출력
3
"""
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
print(numbers.count(5))
"""
문제 12
주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.
입력
word= 'apple'
출력
pple
"""
word= 'apple'
new_word=""
for i in word:
    if i=="a":
        continue
    else:
        new_word+=i
print(new_word)
"""
문제 13
주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
입력
word= 'apple'
출력
eppla
"""
word= 'apple'
new_word2=""
for i in range(len(word)):
    k=word[len(word)-i]
    new_word2+=k
print(new_word2)